import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class IcloudPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10
        self.browseButton_locator = (
            By.XPATH, "//span[contains(text(), 'Browse')]")
        self.recently_deleted_locator = (
            By.XPATH, "//span[contains(text(), 'Recently Deleted')]")
        self.signin_button_locator = (By.CSS_SELECTOR, 'ui-button.sign-in-button')
        self.apple_id_textbox_locator = (By.CSS_SELECTOR, "input#account_name_text_field")
        self.proceed_button_locator = (By.ID, "sign-in")
        self.password_textbox_locator = (By.ID, "password_text_field")
        self.signin_iframe_locator = (By.CSS_SELECTOR, "#aid-auth-widget-iFrame")
        self.iclouddrive_iframe_locator = (By.CSS_SELECTOR, 'iframe[data-name="iclouddrive"]')
        self.delete_button_locator = (
            By.CSS_SELECTOR, 'ui-button[title="Delete"]')


    def icloud_signin(self):


        self.wait_and_execute(self.driver, self.signin_button_locator, 10, lambda elem: elem.click())

        signin_iframe = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        self.signin_iframe_locator)
                )

        self.driver.switch_to.frame(signin_iframe)

        self.wait_and_execute(self.driver, self.apple_id_textbox_locator, 20, lambda elem: (
            elem.click(),
            elem.send_keys(Keys.CONTROL + "a"),
            elem.send_keys(Keys.DELETE),
            elem.send_keys(self.env_icloud_email)
        ))


        # time.sleep(3000)
        # keep_me_signed_in_checkbox_locator = (By.CSS_SELECTOR, '.form-choice-indicator')
        # self.wait_and_execute(self.driver, keep_me_signed_in_checkbox_locator, 20, lambda elem: elem.click())



        self.wait_and_execute(self.driver, self.proceed_button_locator, 10, lambda elem: elem.click())


        self.wait_and_execute(self.driver, self.password_textbox_locator, 10, lambda elem: (
            elem.click(),
            elem.send_keys(Keys.CONTROL + "a"),
            elem.send_keys(Keys.DELETE),
            elem.send_keys(self.env_icloud_password)
        ))
        self.wait_and_execute(self.driver, self.proceed_button_locator, 10, lambda elem: elem.click())
        self.driver.switch_to.default_content()

    def delete_file(self):


        # find the iframe element

        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.iclouddrive_iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)

        browseButton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.browseButton_locator)

        )
        browse_button.click()

        try:
            first_file_locator = (
                By.XPATH, "//span[contains(text(), 'gparted')]")
            first_file = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    first_file_locator)
            )
            first_file.click()


            delete_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    self.delete_button_locator)
            )
            delete_button.click()

        except (NoSuchElementException, TimeoutException):
            print("No File to delete.")

        try:
            recently_deleted_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    self.recently_deleted_locator)
            )
            recently_deleted_button.click()


            delete_all_button_locator = (
                By.XPATH, "//ui-button[contains(text(), 'Delete All')]")
            self.wait_and_execute(self.driver,delete_all_button_locator, 5, lambda elem: elem.click())
            # time.sleep(3000)
            popup_delete_button_locator = (
                By.CSS_SELECTOR, ".alert-button-container .cw-button.primary.destructive")

            self.wait_and_execute(self.driver, popup_delete_button_locator, 5, lambda elem: elem.click())

        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            print("No Recent Files to delete.")


    def run_icloud_upload(self,timeout=180):
        self.driver.get(self.test_sites["icloud_upload"])

        # time.sleep(3000)
        try:
            self.icloud_signin()
        except (NoSuchElementException, TimeoutException):
            pass


        self.delete_file()



        self.driver.get(self.test_sites["icloud_upload"])
        time.sleep(5)
        # find the iframe element
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.iclouddrive_iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)



        browseButton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.browseButton_locator)
        )
        browse_button.click()

        input_element_locator = (By.CSS_SELECTOR, '.upload-input-element')
        input_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                input_element_locator)
        )
        upload_file_dir = os.path.abspath(os.path.join(os.getcwd(), "fixtures/upload_files/gparted.iso"))

        input_element.send_keys(upload_file_dir)


        self.logger(f'\niCloud Upload Started... \n')


        self.timout_while_interact(timeout)

    def run_icloud_download(self, timeout=180):

        self.driver.get(self.test_sites["icloud_download"])


        try:
            self.icloud_signin()
        except (NoSuchElementException, TimeoutException):
            pass

        # find the iframe element
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.iclouddrive_iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)



        browseButton = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                self.browseButton_locator)
        )

        # browse_button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Browse')]")
        browse_button.click()

        first_file_locator = (
            By.XPATH, "//span[contains(text(), 'gparted')]")
        first_file = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                first_file_locator)
        )
        first_file.click()

        self.logger(f'\nStarting iCloud Download test... \n')
        # self.dump_cookies()
        # self.load_cookies()
        time.sleep(timeout)
