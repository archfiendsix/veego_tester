from selenium.webdriver.common.by import By
import os
import pyautogui
import pyautogui as py
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class GoogleMeetPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_googleMeet_conference(self, timeout=50):
        self.driver.get(
            self.test_sites['googleMeet_conference'])
        time.sleep(1)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        time.sleep(2)
        py.moveTo(center_width - (width * (-0.15)), center_height - (height // 4) + (height * (0.28)), duration=0.25)
        pyautogui.click()
        pyautogui.click()
        time.sleep(3)
        self.logger("GoogleMeet conferencing started...")
        self.interaction(timeout)