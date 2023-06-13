import time
import os
import random
import pyautogui as py
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class NetflixMobile(BasePage):
    def __init__(self, mobile_driver, test_sites):
        super().__init__(mobile_driver)
        self.mobile_driver = mobile_driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        # x = py.size()
        # height = x.height
        # width = x.width
        # center_height = x.height // 2
        # center_width = x.width // 2
        # time.sleep(1)
        # py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (0.3)), duration=0.25)
        # pyautogui.click()
        # time.sleep(1)
        time.sleep(timeout)


    def run_netflix_mobile(self, timeout=50):
        self.logger('Starting Netflix Application...')
        self.mobile_driver.start_activity("com.netflix.mediaclient",".ui.launch.UIWebViewActivity")
        time.sleep(3)
        element = self.mobile_driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView/android.view.ViewGroup[4]/android.widget.ImageView')
        element.click()
        time.sleep(3)
        element = self.mobile_driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Play Now"]')
        element.click()
        self.logger('Netflix Download started...')
        self.interaction(timeout)