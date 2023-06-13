
from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import pyautogui as py
class ZoomPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_zoom_conference(self, timeout=50):
        self.driver.get(
            self.test_sites['zoom_conference'])
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ' // *[ @ id = "root"] / div / div / div[1] / div[2] / button').click()
        time.sleep(2)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        py.moveTo(center_width - (width * (-0.02)), center_height - (height // 4) + (height * (-0.18)),duration=0.25)  # arrive to sync left
        pyautogui.click()
        time.sleep(1)

        self.logger("Zoom conferencing started...")

        # pyautogui.click()
        # py.moveTo(center_width - (width * (0.44)), center_height - (height // 4) + (height * (0.88)), duration=0.25)  # arrive to sync left
        # time.sleep(3)
        # pyautogui.click()
        self.interaction(timeout)
