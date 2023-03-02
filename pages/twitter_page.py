import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class TwitterPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def twitter_signin(self):
        loginbutton_locator = (By.CSS_SELECTOR, 'a[href="/login"]')
        username_textbox_locator = (
            By.CSS_SELECTOR, 'input[autocomplete="username"]')
        nextbutton_locator = (By.XPATH, "//span[contains(text(), 'Next')]")
        password_textbox_locator = (
            By.CSS_SELECTOR, 'input[autocomplete="current-password"]')

        login_submit_button_locator = (
            By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')
        self.wait_and_execute(
            self.driver, loginbutton_locator, 10, lambda elem: elem.click())
        self.wait_and_execute(self.driver, username_textbox_locator,
                              10, lambda elem: elem.send_keys(self.env_twitter_email))
        self.wait_and_execute(self.driver, nextbutton_locator,
                              10, lambda elem: elem.click())
        self.wait_and_execute(self.driver, password_textbox_locator,
                              10, lambda elem: elem.send_keys(self.env_twitter_password))
        self.wait_and_execute(self.driver, login_submit_button_locator,
                              10, lambda elem: elem.click())

    def run_twitter_social(self, timeout=180):

        self.driver.get(self.test_sites["twitter_social"])
        # time.sleep(3000)
        try:
            # sign_in_to_google_iframe_locator = (
            #     By.CSS_SELECTOR, 'iframe[title="Sign in with Google Dialog"]')
            # iframe = WebDriverWait(self.driver, 20).until(
            #     EC.presence_of_element_located(
            #         sign_in_to_google_iframe_locator)
            # )
            # self.driver.switch_to.frame(iframe)

            # sign_in_to_google_button = (
            #     By.XPATH, "//div[contains(text(), 'Continue as Veego')]")

            # self.wait_and_execute(
            #     self.driver, sign_in_to_google_button, 10, lambda elem: elem.click())
            pass

        except (NoSuchElementException, TimeoutException):
            try:
                self.twitter_signin()
            except (NoSuchElementException, TimeoutException):
                self.logger("Twitter Already Logged in")

        

        # self.load_cookies()
        # self.twitter_signin(self.env_twitter_email, self.env_twitter_password)
        self.logger(f'\nRunning Twitter Social... \n')
        self.timout_while_interact(timeout)
