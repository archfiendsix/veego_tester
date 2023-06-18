
import pyautogui as py
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class WebexPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_webex_conference(self, timeout=30):
        self.driver.get(self.test_sites['webex_conference'])
        time.sleep(2)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2

        time.sleep(1)
        py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (-0.06)),duration=0.25)  # url's to automation
        self.driver.implicitly_wait(100)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (0.39)), duration=0.25)  # url's to automation
        time.sleep(2)
        pyautogui.click()
        self.driver.implicitly_wait(200)
        time.sleep(2)
        py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (0.68)),duration=0.25)  # arrive to webex app
        time.sleep(8)
        pyautogui.click()
        self.driver.implicitly_wait(200)
        time.sleep(1)
        py.moveTo(center_width - (width * (0.17)), center_height - (height // 4) + (height * (0.88)),   duration=0.25)  # clean
        time.sleep(3)
        pyautogui.click()
        time.sleep(7)
        py.moveTo(center_width - (width * (0.08)), center_height - (height // 4) + (height * (0.05)), duration=0.25)  # arrive to icon of user in chrome
        self.driver.implicitly_wait(200)
        time.sleep(4)
        pyautogui.click()
        time.sleep(2)
        py.moveTo(center_width - (width * (-0.13)), center_height - (height // 4) + (height * (0.43)), duration=0.25)  # url's to automation
        self.driver.implicitly_wait(100)
        time.sleep(4)
        pyautogui.click()
        time.sleep(12)

        self.logger("webex conferencing started...")
        self.interaction(timeout)