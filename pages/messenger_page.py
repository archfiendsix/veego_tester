import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

    def run_messenger_conference(self, timeout=180):
        self.logger(f'\nStarting Messenger Conferencing test... \n')
        self.driver.get(self.test_sites["messenger_caller"])
        time.sleep(4)
        ace_veeg_locator = (
            By.XPATH, "//span[contains(text(), 'Ace Veeg')]")
        ace_veeg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                ace_veeg_locator)
        )
        ace_veeg.click()
        start_conference_locator = (
            By.CSS_SELECTOR, 'div[aria-label="Start a video call"]')
        start_conference_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                start_conference_locator)
        )

        action_chains = ActionChains(self.driver)
        action_chains.key_down(Keys.CONTROL).click(start_conference_button).key_up(Keys.CONTROL).perform()

        
        self.driver.switch_to.new_window('tab')
        self.driver.get(self.test_sites["messenger_receiver"])
        # self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.window(self.driver.window_handles[-2])
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
        
