import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class MessengerPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.messenger_email_textbox_locator = (By.CSS_SELECTOR, 'input[name="email"]')
        self.messenger_password_texbox_locator = (By.CSS_SELECTOR, 'input#pass')
        self.messenger_continue_button_locator = (By.CSS_SELECTOR, '#loginbutton')
        self.keep_me_signed_in_label = (By.XPATH, "//label[contains(text(), 'Keep me signed in')]")

    def run_messenger_conference(self, timeout=180):
        self.logger(f'\nStarting Messenger Conferencing test... \n')



        # time.sleep(3000)



        try:
            print("Detecting Login State...")
            self.driver.get(self.test_sites["messenger_caller"])
            self.wait_and_execute(self.driver, self.messenger_email_textbox_locator, 10, lambda elem: (elem.click(), elem.send_keys(Keys.CONTROL+"a"), elem.send_keys(Keys.DELETE), elem.send_keys(self.env_messenger_email)))
            self.wait_and_execute(self.driver, self.messenger_password_texbox_locator, 10, lambda elem: (elem.click(), elem.send_keys(Keys.CONTROL+"a"), elem.send_keys(Keys.DELETE), elem.send_keys(self.env_messenger_password)))
            self.wait_and_execute(self.driver,self.keep_me_signed_in_label, 10, lambda elem:elem.click())
            self.wait_and_execute(self.driver, self.messenger_continue_button_locator, 10, lambda elem: elem.click())


        except (NoSuchElementException, TimeoutException):
            print("User already logged in")

        try:
            self.driver.switch_to.new_window('tab')
            self.driver.get(self.test_sites["messenger_receiver"])

            self.wait_and_execute(self.driver, self.messenger_email_textbox_locator, 30, lambda elem: (
                elem.click(), elem.send_keys(Keys.CONTROL + "a"), elem.send_keys(Keys.DELETE),
                elem.send_keys(self.env_facebook_email)))
            self.wait_and_execute(self.driver, self.messenger_password_texbox_locator, 30, lambda elem: (
                elem.click(), elem.send_keys(Keys.CONTROL + "a"), elem.send_keys(Keys.DELETE),
                elem.send_keys(self.env_facebook_password)))
            # time.sleep(3000)
            # self.wait_and_execute(self.driver, self.keep_me_signed_in_label, 30, lambda elem: elem.click())
            self.wait_and_execute(self.driver, self.messenger_continue_button_locator, 30, lambda elem: elem.click())
        except (NoSuchElementException, TimeoutException):
            print("User already logged in")

        self.driver.switch_to.window(self.driver.window_handles[0])
        ace_veeg_locator = (
            By.XPATH, "//span[contains(text(), 'Ace Veeg')]")
        ace_veeg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                ace_veeg_locator)
        )

        self.driver.switch_to.window(self.driver.window_handles[0])
        ace_veeg.click()

        start_conference_locator = (
            By.CSS_SELECTOR, 'div[aria-label="Start a video call"]')
        start_conference_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                start_conference_locator)
        )

        action_chains = ActionChains(self.driver)
        action_chains.key_down(Keys.CONTROL).click(start_conference_button).key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[-1])



        self.driver.switch_to.window(self.driver.window_handles[-2])
        self.driver.get(self.test_sites["messenger_receiver"])
        # self.driver.switch_to.window(self.driver.window_handles[-2])
        accept_button_locator = (
            By.CSS_SELECTOR, 'div[aria-label="Accept"]')
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                accept_button_locator)
        )

        time.sleep(6)
        action_chains = ActionChains(self.driver)
        action_chains.key_down(Keys.CONTROL).click(accept_button).key_up(Keys.CONTROL).perform()

        self.driver.switch_to.window(self.driver.window_handles[-2])
        self.logger(f'\nMessenger Conferencing started... \n')
        time.sleep(timeout)
        
