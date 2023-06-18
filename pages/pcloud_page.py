from selenium.webdriver.common.by import By
import os
import pyautogui as py
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

    def run_pcloud_upload(self, timeout=50):
        self.driver.get( self.test_sites['pcloud_upload'])
        time.sleep(5)
        # time.sleep(3000)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div[3]/div[1]').click()
        time.sleep(1)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        time.sleep(1)
        py.moveTo(center_width - (width * (0.18)), center_height - (height // 4) + (height * (0.59)), duration=0.25)
        pyautogui.click()
        time.sleep(1)
        # py.moveTo(center_width - (width * (0.47)), center_height - (height // 4) + (height * (-0.03)), duration=0.25)
        # pyautogui.click()
        time.sleep(1)
        py.moveTo(center_width - (width * (0.33)), center_height - (height // 4) + (height * (-0.08)), duration=0.25)
        pyautogui.click()
        pyautogui.click()
        time.sleep(1)
        self.logger("Pcloud upload started...")
        self.interaction(timeout)

    def run_pcloud_download(self, timeout=50):
        self.driver.get(self.test_sites['pcloud_upload'])
        time.sleep(5)
        # time.sleep(3000)
        time.sleep(1)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        time.sleep(1)
        py.moveTo(center_width - (width * (0.18)), center_height - (height // 4) + (height * (0.35)), duration=0.25)
        pyautogui.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,  '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/div[3]/span').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,  ' / html/body/div[14]/div/div/div/form/div[5]/a[2]/span').click()


        # py.moveTo(center_width - (width * (-0.07)), center_height - (height // 4) + (height * (0.18)), duration=0.25)
        # pyautogui.click()
        time.sleep(10)
        self.logger("Pcloud download started...")
        self.interaction(timeout)