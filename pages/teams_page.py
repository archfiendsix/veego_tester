
import pyautogui as py

import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class TeamsPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_teams_conference(self, timeout):
        self.driver.get(self.test_sites['teams_conference'])
        time.sleep(5)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        py.moveTo(center_width - (width * (-0.005)), center_height - (height // 4) + (height * (0.3)), duration=0.25)
        time.sleep(5)
        # pyautogui.click()
        # time.sleep(1)
        #
        # py.moveTo(center_width - (width * (0.005)), center_height - (height // 4) + (height * (0.36)), duration=0.25)
        # time.sleep(5)
        # pyautogui.click()
        # time.sleep(1)



        self.logger("teams conferencing started...")
        self.interaction(timeout)






#
# import time
# from pathlib import Path
# from turtle import update
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import undetected_chromedriver as ucdriver
# import pyautogui as py
#
#
# import pyautogui
# import pytest
# from selenium.webdriver.support.ui import WebDriverWait
# import selenium
# from selenium.common.exceptions import NoSuchElementException
#
# from selenium.webdriver.chrome.options import Options
#
# import urllib3
# from selenium import webdriver
# #from webdriver_auto_update import check_driver
#
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = ucdriver.Chrome()
# time.sleep(1)
# driver.get('https://teams.live.com/meet/9433508200836')
# driver.maximize_window()
# driver.implicitly_wait(300)
# time.sleep(2)
# pyautogui.click()
# time.sleep(120)
#
# x = py.size()
# height = x.height
# width = x.width
# center_height = x.height // 2
# center_width = x.width // 2
# py.moveTo(center_width - (width * (0.03590)), center_height - (height // 4) + (height * (0.05)), duration=0.25)
# time.sleep(5)
# pyautogui.click()
# py.click()
# time.sleep(2)
# # driver(os.close)
# py.moveTo(center_width - (width * (- 0.0010)), center_height - (height // 4) + (height * (0.552)), duration=0.25)
# time.sleep(5)
# pyautogui.click()
# py.click()
# time.sleep(60)