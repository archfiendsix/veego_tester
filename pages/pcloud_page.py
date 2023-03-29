from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class PcloudPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_pcloud_upload(self, timeout):
        self.driver.get( self.test_sites['pcloud_upload'])
        time.sleep(5)
        # time.sleep(3000)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div[3]/div[1]').click()
        time.sleep(29)
        # self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[3]/div[2]/div[1]/div/input').click()
        self.logger("Pcloud upload started...")
        self.interaction(timeout)