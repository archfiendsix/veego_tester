import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class IcloudPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def icloud_signin(self):
        signin_button_locator = (By.CSS_SELECTOR, 'ui-button.sign-in-button')

        self.wait_and_execute(self.driver, signin_button_locator, 10, lambda elem: elem.click())
        signin_iframe_locator = (By.CSS_SELECTOR, "#aid-auth-widget-iFrame")
        signin_iframe = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        signin_iframe_locator)
                )


        self.driver.switch_to.frame(signin_iframe)
        apple_id_textbox_locator = (By.CSS_SELECTOR, "input#account_name_text_field")
        self.wait_and_execute(self.driver, apple_id_textbox_locator, 20, lambda elem: (
            elem.click(),
            elem.send_keys(Keys.CONTROL + "a"),
            elem.send_keys(Keys.DELETE),
            elem.send_keys(self.env_icloud_email)
        ))

        # time.sleep(3000)
        keep_me_signed_in_checkbox_locator = (By.CSS_SELECTOR, 'input[type="checkbox"]')
        self.wait_and_execute(self.driver, keep_me_signed_in_checkbox_locator, 10, lambda elem: elem.click())

        proceed_button_locator = (By.ID, "sign-in")
        self.wait_and_execute(self.driver, proceed_button_locator, 10, lambda elem: elem.click())

        password_textbox_locator = (By.ID, "password_text_field")
        self.wait_and_execute(self.driver, password_textbox_locator, 10, lambda elem: (
            elem.click(),
            elem.send_keys(Keys.CONTROL + "a"),
            elem.send_keys(Keys.DELETE),
            elem.send_keys(self.env_icloud_password)
        ))
        self.wait_and_execute(self.driver, proceed_button_locator, 10, lambda elem: elem.click())
        self.driver.switch_to.default_content()

    def delete_file(self):
        self.driver.get(self.test_sites["icloud_upload"])

        self.driver.maximize_window()
        time.sleep(15)
        # find the iframe element
        iframe_locator = (By.CSS_SELECTOR, 'iframe[data-name="iclouddrive"]')
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)

        browseButton_locator = (
            By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                browseButton_locator)
        )
        browseButton.click()

        first_file_locator = (
            By.CSS_SELECTOR, 'div[role="listitem"]')
        first_file = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                first_file_locator)
        )
        first_file.click()

        delete_button_locator = (
            By.CSS_SELECTOR, 'ui-button[title="Delete"]')
        delete_button = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                delete_button_locator)
        )
        delete_button.click()

        # self.dump_cookies()
        # self.load_cookies()

    def run_icloud_upload(self,timeout=180):
        self.driver.get(self.test_sites["icloud_upload"])
        self.icloud_signin()
        # try:
        #     self.icloud_signin()
        # except (NoSuchElementException, TimeoutException):
        #     pass

        self.delete_file()

        self.driver.get(self.test_sites["icloud_upload"])

        self.driver.maximize_window()
        time.sleep(15)
        # find the iframe element
        iframe_locator = (By.CSS_SELECTOR, 'iframe[data-name="iclouddrive"]')
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)

        browseButton_locator = (
            By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                browseButton_locator)
        )
        browseButton.click()

        input_element_locator = (By.CSS_SELECTOR, '.upload-input-element')
        input_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                input_element_locator)
        )

        input_element.send_keys("fixtures/upload_files/gparted.iso")

        self.logger(f'\nStarting iCloud Upload test... \n')
        # self.dump_cookies()
        # self.load_cookies()
        #

        time.sleep(timeout)

    def run_icloud_download(self, timeout=180):
        # self.icloud_signin(self.env_nexusmods_email, self.env_nexusmods_password)

        self.driver.get(self.test_sites["icloud_download"])
        # time.sleep(3000)
        self.driver.maximize_window()
        # find the iframe element
        iframe_locator = (By.CSS_SELECTOR, 'iframe[data-name="iclouddrive"]')
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)

        browseButton_locator = (
            By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                browseButton_locator)
        )

        # browseButton = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton.click()

        first_file_locator = (
            By.XPATH, "//span[contains(text(), 'gparted-…-amd64')]")
        first_file = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                first_file_locator)
        )
        first_file.click()

        self.logger(f'\nStarting iCloud Download test... \n')
        # self.dump_cookies()
        # self.load_cookies()
        time.sleep(timeout)
