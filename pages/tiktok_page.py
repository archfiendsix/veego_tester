import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage

class TiktokPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def tiktok_signin(self):

        try:
            self.wait_and_execute(
                self.driver, (By.CSS_SELECTOR, 'button[data-e2e="top-login-button"]'), 5, lambda elem: elem.click())
            # time.sleep(3000)
            self.wait_and_execute(
                self.driver, (By.XPATH, "//p[contains(text(), 'Use phone / email / username')]"), 5,
                lambda elem: elem.click())
            self.wait_and_execute(
                self.driver, (By.CSS_SELECTOR, 'a[href="/login/phone-or-email/email"]'), 5,
                lambda elem: elem.click())

            self.wait_and_execute(self.driver, (By.CSS_SELECTOR, 'input[name="username"]'),
                                  20, lambda elem: elem.send_keys(Keys.CONTROL + "a"))

            self.wait_and_execute(self.driver, (By.CSS_SELECTOR, 'input[name="username"]'),
                                  20, lambda elem: elem.send_keys(Keys.DELETE))

            self.wait_and_execute(
                self.driver, (By.CSS_SELECTOR, 'input[name="username"]'), 5,
                lambda elem: elem.send_keys(self.env_tiktok_username))

            self.wait_and_execute(self.driver, (By.CSS_SELECTOR, 'input[placeholder="Password"]'),
                                  20, lambda elem: elem.send_keys(Keys.CONTROL + "a"))

            self.wait_and_execute(self.driver, (By.CSS_SELECTOR, 'input[placeholder="Password"]'),
                                  20, lambda elem: elem.send_keys(Keys.DELETE))

            self.wait_and_execute(
                self.driver, (By.CSS_SELECTOR, 'input[placeholder="Password"]'), 5,
                lambda elem: elem.send_keys(self.env_tiktok_password))

            self.wait_and_execute(
                self.driver, (By.CSS_SELECTOR, 'a+button[data-e2e="login-button"]'), 5,
                lambda elem: elem.click())

        except (NoSuchElementException, TimeoutException):
            pass

    def interaction(self, timeout=180):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.random_scroll(timeout)

    def run_tiktok_social(self, timeout=180):

        self.driver.get(self.test_sites["tiktok_social"])

        self.tiktok_signin()

        self.logger(f'\nRunning Tiktok Social... \n')

        self.interaction(timeout)
