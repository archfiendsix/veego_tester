import time
import os
import pyautogui as py
import pyautogui
import random
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


class SkypeMobile(BasePage):
    def __init__(self, mobile_driver, test_sites):
        super().__init__(mobile_driver)
        self.mobile_driver = mobile_driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        # # Get the dimensions of the screen
        # width = self.mobile_driver.get_window_size()['width']
        # height = self.mobile_driver.get_window_size()['height']
        #
        # start_time = time.time()
        # self.logger('Interacting with Skype application...')
        # while time.time() - start_time < timeout:
        #     # Wait for a random time between 0 and 10 seconds
        #     time.sleep(random.randint(0, 5))  # wait for n seconds between scrolls
        #
        #     # Calculate the start and end coordinates for the swipe
        #     start_x = width / 2
        #     start_y = height / 2
        #     end_x = start_x
        #     end_y = start_y - (height * 0.1)  # move in the opposite direction
        #
        #     # Perform the swipe action
        #     action = TouchAction(self.mobile_driver)
        #     action.press(x=start_x, y=start_y).wait(200).move_to(x=end_x, y=end_y).release().perform()
        time.sleep(timeout)

    def run_skype_mobile(self, timeout=50):
        self.logger('Starting Skype Application...')
        self.mobile_driver.start_activity("com.skype.raider","com.skype4life.MainActivity")
        time.sleep(5)
        actions = ActionChains(self.mobile_driver)
        time.sleep(1)
        actions.w3c_actions.pointer_action.move_to_location(410, 1020)
        actions.click()
        actions.perform()
        time.sleep(2)

        actions0 = ActionChains(self.mobile_driver)
        actions0.w3c_actions.pointer_action.move_to_location(500, 200)
        actions0.click()
        actions0.perform()
        time.sleep(2)


        actions1 = ActionChains(self.mobile_driver)
        time.sleep(3)
        actions1.w3c_actions.pointer_action.move_to_location(210, 1180)
        actions1.click()
        actions1.perform()
        time.sleep(2)

        actions2 = ActionChains(self.mobile_driver)
        time.sleep(3)
        actions2.w3c_actions.pointer_action.move_to_location(550, 1960)
        actions2.click()
        actions2.perform()
        time.sleep(5)

      #####web######################
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        # py.moveTo(center_width - (width * (-0.45)), center_height - (height // 4) + (height * (0.68)), duration=0.25)
        # time.sleep(2)
        # pyautogui.click()
        # time.sleep(2)
        py.moveTo(center_width - (width * (-0.22)), center_height - (height // 4) + (height * (-0.0522)), duration=0.25)
        time.sleep(1)
        pyautogui.click()
        py.moveTo(center_width - (width * (-0.01)), center_height - (height // 4) + (height * (0.43)), duration=0.25)
        time.sleep(2)
        # pyautogui.click()
        # pyautogui.click()
        # time.sleep(1)

        self.logger('Skype application started...')
        self.interaction(timeout)