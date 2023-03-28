from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class ZoomPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_zoom_conference(self, timeout):
        self.driver.get(
            self.test_sites['zoom_conference'])
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/h2/a').click()
        time.sleep(1)
        self.logger("Zoom conferencing started...")
        self.interaction(timeout)
