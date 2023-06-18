from selenium.webdriver.common.by import By
import os
import pyautogui as py
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class GoogledrivePage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_googledrive_upload(self, timeout=50):
        self.driver.get( self.test_sites['googledrive'])
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        py.moveTo(center_width - (width * (0.44)), center_height - (height // 4) + (height * (-0.03)),duration=0.25)  # arrive to webex app
        time.sleep(2)
        pyautogui.click()
        time.sleep(3)
        py.moveTo(center_width - (width * (0.44)), center_height - (height // 4) + (height * (0.03)),duration=0.25)  # arrive to sync
        self.driver.implicitly_wait(300)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        ####
        py.moveTo(center_width - (width * (0.33)), center_height - (height // 4) + (height * (-0.09)),  duration=0.25)  # arrive to sync
        self.driver.implicitly_wait(300)
        time.sleep(2)
        pyautogui.click()
        pyautogui.click()
        time.sleep(2)
        self.logger("Googledrive upload started...")
        self.interaction(timeout)

    def run_googledrive_download(self, timeout=50):
        self.driver.get(self.test_sites['googledrive'])
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        py.moveTo(center_width - (width * (0.44)), center_height - (height // 4) + (height * (-0.03)),  duration=0.25)  # arrive to webex app
        time.sleep(2)
        pyautogui.click()
        time.sleep(3)
        py.moveTo(center_width - (width * (0.44)), center_height - (height // 4) + (height * (0.03)), duration=0.25)  # arrive to sync
        self.driver.implicitly_wait(300)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        ####
        py.moveTo(center_width - (width * (0.33)), center_height - (height // 4) + (height * (-0.09)),   duration=0.25)  # arrive to sync
        self.driver.implicitly_wait(300)
        time.sleep(2)
        pyautogui.click()
        pyautogui.click()
        self.logger("Googledrive download started...")
        self.interaction(timeout)