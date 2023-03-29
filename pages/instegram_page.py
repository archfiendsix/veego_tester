from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class InstegramPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites

    def instegram_signin(self):
        self.driver.switch_to.default_content()

        # self.wait_and_execute(
        #     self.driver, (By.CSS_SELECTOR, 'a[data-testid="loginButton"]'), 10, lambda elem: elem.click())
        # time.sleep(3000)
        self.wait_and_execute(
            self.driver, (By.CSS_SELECTOR, 'input[autocomplete="username"]'), 5,
            lambda elem: elem.send_keys(self.env_instegram_email))

        self.wait_and_execute(
            self.driver, (By.XPATH, "//span[contains(text(), 'Next')]"), 5,
            lambda elem: elem.click())

        self.wait_and_execute(
            self.driver, (By.CSS_SELECTOR, 'input[type="password"]'), 5,
            lambda elem: elem.send_keys(self.env_instegram_password))

        self.wait_and_execute(
            self.driver, (By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]'), 5, lambda elem: elem.click())

    def interaction(self, timeout=180):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.random_scroll(timeout)

    def run_instegram_social(self, timeout=180):

        self.driver.get(self.test_sites["instegram_social"])

        try:
            signin_iframe_locator = (By.CSS_SELECTOR, 'iframe[title="Sign in with Google Dialog"]')
            signin_iframe = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    signin_iframe_locator)
            )

            self.driver.switch_to.frame(signin_iframe)

            continue_as = (By.CSS_SELECTOR, '#continue-as')

            self.wait_and_execute(self.driver, continue_as, 5, lambda elem: elem.click())
        except(NoSuchElementException, TimeoutException):
            pass

        # self.twitter_signin(self.env_facebook_email, self.env_facebook_password)
        self.logger(f'\nRunning Instegram Social... \n')
        self.interaction(timeout)