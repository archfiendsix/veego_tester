

from selenium.webdriver.common.by import By
import os
import pyautogui as py
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class NetflixPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_netflix_streaming(self, timeout):
        self.driver.get(
            self.test_sites['netflix_streaming'])
        time.sleep(5)

        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        time.sleep(1)
        py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (0.3)), duration=0.25)
        pyautogui.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="main-view"]/div/span/div/div/div/div/div/div[2]/div/div/div[3]/a[2]/button').click()
        time.sleep(1)

        self.logger("Netflix streaming started...")
        self.interaction(timeout)

