from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class SpeedPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_speed_download(self, timeout):
        self.driver.get( self.test_sites['speed_download'])
        time.sleep(5)
        # time.sleep(3000)
        self.driver.find_element(By.XPATH, '/html/body/p[3]/a').click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH,' // *[ @ id = "maestro-content-portal"] / div / div / div / div / div / div[2] / div[1] / div / div[4] / button / span').click()
        self.logger("Speed download started...")
        self.interaction(timeout)