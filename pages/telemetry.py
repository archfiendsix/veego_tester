import time
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

load_dotenv()


class Telemetry(BasePage):
    def __init__(self, driver, config_data):
        super().__init__(driver)
        self.driver = driver
        self.config_data = config_data
        self.login_texbox_locator = (By.ID, "username")

    # Define the login method
    def run_telemetry(self):
        self.logger("Starting Telemetry...")
        self.driver.switch_to.new_window('tab')
        self.driver.get(
            self.config_data["telemetry"] + self.config_data["router_id"])
        try:

            login_textbox_locator = (By.ID, "username")
            login_tb_attrib = self.wait_and_execute(
                self.driver, login_textbox_locator, 20, lambda elem: elem.get_attribute("value"))
            # Check if the login textbox is already populated with the correct value
            if login_tb_attrib != self.env_username:
                # login_textbox.send_keys(Keys.CONTROL + "a")
                self.wait_and_execute(self.driver, login_textbox_locator,
                                      20, lambda elem: elem.send_keys(Keys.CONTROL + "a"))
                # login_textbox.send_keys(Keys.DELETE)
                self.wait_and_execute(self.driver, login_textbox_locator,
                                      20, lambda elem: elem.send_keys(Keys.DELETE))
                # login_textbox.send_keys(self.env_username)
                self.wait_and_execute(self.driver, login_textbox_locator,
                                      20, lambda elem: elem.send_keys(self.env_username))

            password_textbox = self.driver.find_element(By.ID, "password")
            # Check if the password textbox is already populated with the correct value
            if password_textbox.get_attribute("value") != self.env_password:
                password_textbox.send_keys(Keys.CONTROL + "a")
                password_textbox.send_keys(Keys.DELETE)
                password_textbox.send_keys(self.env_password)

            login_button = self.driver.find_element(By.ID, "kc-login")
            login_button.click()
        except (NoSuchElementException, TimeoutException):
            # Elements not found, so the user is probably already signed in
            pass

    def return_page_service_items(self, name, type, is_classification_final):
        # Switch to telemetry Window
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        service_items = None

        body = self.driver.find_element(By.CSS_SELECTOR, "body")
        body_text = body.text

        try:
            text_to_json = json.loads(body_text)
        except json.decoder.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON data: {e}")
            return

        services = text_to_json["devices"][0]["discovery"]["devices"][self.config_data["mac"]]["services"]
        assert services, "No running services detected"
        service_items = {key: value for key, value in services.items(
        ) if value["type"] == type}
        # value["is_classification_final"] == is_classification_final and
        # and value[
        #         "name"] == name
        return service_items

    def test_service_test(self, rerun, detected_service_name, service_name, detected_service_type
                          , is_classifcation_final, service_type, uuid_key, service_start_time, delta, score):

        self.logger(
            f"\n {rerun}.) {detected_service_name} {detected_service_type} started at: {service_start_time}\n"
            f"\nName: {detected_service_name}\nService Type: {detected_service_type}\nRecognized in: {delta} "
            f"Minutes\nService UUID: {uuid_key}\n" f"Score: {score}\n" f"Is classification final: "
            f"{is_classifcation_final}")

        # Check if service is correct and log message accordingly
        if detected_service_name == service_name and detected_service_type == service_type:
            assert True
            self.logger("PASS: Both type and name are correct\n\n")
        elif detected_service_type == service_type and (
                not detected_service_name or detected_service_name == ''):
            assert True
            self.logger(
                "Partial PASS: Type is correct, name is empty\n\n")
        elif detected_service_type == service_type and detected_service_name != service_name:
            self.logger(
                "Fail: Type is correct, name is incorrect\n\n")
        else:
            self.logger("Fail: Type and/or name are incorrect\n\n")

    def run_telemetry_test(self, service_name, service_type, classification_final, interaction):

        self.run_telemetry()
        self.logger("\nLooking for services...\n")
        # Initialize variables
        rerun = 0
        max_runtime = 3 * 60  # 6 minutes in seconds
        detection_time = datetime.utcnow()

        # Loop until maximum runtime is reached
        while (datetime.utcnow() - detection_time).total_seconds() <= max_runtime:
            # Try to detect the service
            service_item = self.return_page_service_items(
                service_name, service_type, classification_final)

            # Loop until service is detected or maximum runtime is reached
            while service_item:
                # Print information about detected service
                uuid_key = next(iter(service_item))
                detected_service_name = service_item[uuid_key]['name']
                detected_service_type = service_item[uuid_key]['type']
                detected_is_classification_final = service_item[uuid_key]['is_classification_final']
                service_start_time = datetime.utcfromtimestamp(
                    service_item[uuid_key]['start_time'] / 1000)
                delta = detection_time - service_start_time
                detected_score = service_item[uuid_key]['score']

                self.test_service_test(rerun, detected_service_name, service_name, detected_service_type, detected_is_classification_final, service_type, uuid_key, service_start_time, delta, detected_score)

                # Wait before trying to detect service again
                interaction(10)

                # Check if maximum runtime has been reached and exit if it has
                if (datetime.utcnow() - detection_time).total_seconds() > max_runtime:
                    self.logger("Maximum runtime exceeded, exiting function")
                    return

                # Try to detect the service again
                rerun += 1
                service_item = self.return_page_service_items(
                    service_name, service_type, classification_final)

            # Print message if service is not detected within the allowed time
            total_testing_time = datetime.utcnow() - detection_time
            if total_testing_time.total_seconds() >= 120 and not service_item:
                total_testing_time = total_testing_time / 60
                self.logger(
                    f"No {service_name} service recognized for the past {total_testing_time} minutes\n")
                assert False
                return

            # Wait before trying to detect service again
            rerun += 1
            interaction(10)

            if (datetime.utcnow() - detection_time).total_seconds() <= max_runtime:
                self.logger(f"FAIL: No {service_name} {service_type} service detected. Retrying service "
                            f"recognition test ({rerun})...\n")
            else:
                assert False
