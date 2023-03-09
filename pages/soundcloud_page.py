import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class SoundcloudPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10
        self.header_sign_button_locator = (By.CSS_SELECTOR, '.header__loginMenu button[title="Sign in"]')
        self.accept_cookies_button_locator = (By.ID, 'onetrust-accept-btn-handler')
        self.signin_email_textbox_locator = (By.CSS_SELECTOR, '#sign_in_up_email')
        self.signin_continue_button_locator = (By.CSS_SELECTOR, 'button[title="Continue"]')
        self.signin_password_textbox_locator = (By.ID, 'enter_password_field')
        self.signin_signin_button_locator = (By.ID, 'enter_password_submit')

    def soundcloud_signin(self):


        try:
            self.wait_and_execute(self.driver, self.header_sign_button_locator, 30, lambda elem: elem.click())
            # time.sleep(3000)
            # Find all iframes on the page
            iframes = self.driver.find_elements(By.CSS_SELECTOR, "iframe")

            # Iterate over each iframe
            for iframe in iframes:
                # Check if the src attribute includes the expected URL
                if "https://secure.soundcloud.com/web-auth" in iframe.get_attribute("src"):
                    # Switch to the iframe
                    self.driver.switch_to.frame(iframe)
                    break  # Stop iterating over iframes once we have found the correct one


            self.wait_and_execute(self.driver, self.signin_email_textbox_locator, 60,
                                  lambda elem:( elem.click(), elem.send_keys(Keys.CONTROL+"a"), elem.send_keys(Keys.DELETE)))
            self.wait_and_execute(self.driver, self.signin_email_textbox_locator, 60, lambda elem: elem.send_keys(self.env_soundcloud_email))
            self.wait_and_execute(self.driver, self.signin_continue_button_locator, 30, lambda  elem: elem.click())
            self.wait_and_execute(self.driver, self.signin_password_textbox_locator, 30, lambda  elem: (elem.click(), elem.send_keys(Keys.CONTROL+"a"), elem.send_keys(Keys.DELETE),elem.send_keys(self.env_soundcloud_password)))
            self.wait_and_execute(self.driver, self.signin_signin_button_locator, 30, lambda elem: elem.click())
        except (NoSuchElementException, TimeoutException):
            pass
        try:
            # Wait for the alert to appear
            alert = Alert(self.driver)
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Switch to the alert box and click the "Save" button
            alert.accept()

        except(NoSuchElementException, TimeoutException):
            pass

        self.driver.switch_to.default_content()
    def run_soundcloud_music(self, timeout=180):


        self.driver.get(self.test_sites["soundcloud_music"])
        time.sleep(5)
        play_btn_locator = (
            By.CSS_SELECTOR, ".sc-button-play.playButton.sc-button.m-stretch")

        self.wait_and_execute(self.driver, play_btn_locator, 30, lambda elem: elem.click())

        # time.sleep(10)
        try:
            self.wait_and_execute(self.driver, self.accept_cookies_button_locator, 30, lambda elem: elem.click())

        except (NoSuchElementException, TimeoutException):
            pass

        # self.soundcloud_signin()
        try:
            self.soundcloud_signin()
        except (NoSuchElementException, TimeoutException):
            pass

        try:
            self.driver.get(self.test_sites["soundcloud_music"])
            play_btn_locator = (
                By.CSS_SELECTOR, ".sc-button-play.playButton.sc-button.m-stretch")

            self.wait_and_execute(self.driver,play_btn_locator,20,lambda elem: elem.click())



        except StaleElementReferenceException:
            pass

        self.logger(f'\nStarting Soundcloud play test... \n')
        self.timout_while_interact(timeout)

    def run_soundcloud_upload(self, timeout=180):
        self.logger('Starting Soundcloud upload test...')

        # Load the Soundcloud upload page
        self.driver.maximize_window()
        self.driver.get(self.test_sites["soundcloud_upload"])
        self.soundcloud_signin()
        self.driver.get(self.test_sites["soundcloud_upload"])
        time.sleep(3)


        # Select the file to upload
        file_input_locator = (
            By.CSS_SELECTOR, ".chooseFiles .chooseFiles__input")
        file_upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(file_input_locator)
        )
        file_path = os.path.abspath("fixtures/upload_files/music.mp3")
        file_upload_input.send_keys(file_path)

        save_button_locator = (By.CSS_SELECTOR, 'button[title="Save"]')
        save_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(save_button_locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", save_button)
        save_button.click()
        # self.dump_cookies()
        # self.load_cookies()
        # Wait for the upload to complete
        time.sleep(timeout)

        # 180
