import logging
import os
import pathlib
import time
from pathlib import Path
import pyautogui
import pyautogui as py
# import undetected_chromedriver.v2 as uc
import undetected_chromedriver as ucdriver
from selenium.webdriver.common.by import By

import urllib3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


#
# from infra.agent_connectivity.ui_connectivity import ui_connectivity
# from infra.constants import DEVICES_TAB_XPATH, GOOGLE_MEET_NAME_ENTER, GOOGLE_MEET_EMAIL_NAME, \
#     GOOGLE_MEET_EMAIL_TEXTFIELD, GOOGLE_MEET_PASSWORD, GOOGLE_MEET_NEXT_BUTTON


class TwitchPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_twitch_streaming(self, timeout=180):
        # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # driver = webdriver.Chrome()
        # driver = webdriver.Chrome(executable_path='C:/Veego/Automation/chromedriver.exe')

        self.driver.get(self.test_sites['twitch_streaming'])
        self.driver.maximize_window()

        # return driver
        # driver.close()
        # driver.quit()
        self.actions.send_keys('k').perform()
        self.logger(f'\nRunning Twitch Streaming... \n')

        self.interaction(timeout)
        # 180


#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# driver = webdriver.Chrome()
# # driver = webdriver.Chrome(executable_path='C:/Veego/Automation/chromedriver.exe')
# for _ in range(5):
#     try:
#         driver.get('https://www.twitch.tv/videos/1733916001')
#         time.sleep(122)
#         # return driver
#         # driver.close()
#         # driver.quit()
#         break
#     except BaseException as e:
#         # logger.warning(e.msg)
#         time.sleep(3)
#         continue
#     else:
#         break
# else:
#     driver.close()


