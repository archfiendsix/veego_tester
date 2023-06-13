
import pyautogui as py
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class SkypePage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_skype_conference(self, timeout=30):
        self.driver.get(self.test_sites['skype_conference'])
        time.sleep(7)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (0.29)), duration=0.25)
        time.sleep(5)
        pyautogui.click()
        time.sleep(1)
        py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (0.46)), duration=0.25)
        time.sleep(3)
        pyautogui.click()
        time.sleep(1)
        # # #
        py.moveTo(center_width - (width * (0.005)), center_height - (height // 4) + (height * (0.26)), duration=0.25)
        time.sleep(5)
        pyautogui.click()
        time.sleep(2)
        py.moveTo(center_width - (width * (-0.012)), center_height - (height // 4) + (height * (0.49)), duration=0.25)
        time.sleep(10)
        pyautogui.click()
        self.logger("skype conferencing started...")
        self.interaction(timeout)