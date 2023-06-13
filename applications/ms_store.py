import os
import time
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MSStore(BasePage):

    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10
        self.get_in_store_app_button_locator = (By.CSS_SELECTOR, 'div[aria-label="Get Ubuntu in Store app"]')

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_msstore_download(self, timeout=50):
        self.driver.get(self.test_sites["msstore_download"])
        self.wait_and_execute(self.driver, self.get_in_store_app_button_locator, 10, lambda elem: elem.click())
        time.sleep(3)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(3)
        self.open_window("Microsoft Store")
        # self.application_action("Microsoft Store", "Get")
        time.sleep(5)

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        # pyautogui.press('tab')
        pyautogui.press('enter')
        self.interaction(timeout)
