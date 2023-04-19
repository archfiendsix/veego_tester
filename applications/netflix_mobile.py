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
    '''
    def interaction(self, timeout):
        # Get the dimensions of the screen
        width = self.mobile_driver.get_window_size()['width']
        height = self.mobile_driver.get_window_size()['height']

        start_time = time.time()
        self.logger('Interacting with Youtube application...')
        while time.time() - start_time < timeout:
            # Wait for a random time between 0 and 10 seconds
            time.sleep(random.randint(0, 5))  # wait for n seconds between scrolls

            # Calculate the start and end coordinates for the swipe
            start_x = width / 2
            start_y = height / 2
            end_x = start_x
            end_y = start_y - (height * 0.1)  # move in the opposite direction

            # Perform the swipe action
            action = TouchAction(self.mobile_driver)
            action.press(x=start_x, y=start_y).wait(200).move_to(x=end_x, y=end_y).release().perform()
        time.sleep(timeout)
    '''

    def run_netflix_mobile(self, timeout=50):
        self.logger('Starting Netflix Application...')
        self.mobile_driver.start_activity("com.netflix.mediaclient","o.bWS")
        time.sleep(1)
        # self.driver.find_element("com.google.android.youtube", "com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity")
        self.logger('Netflix application started...')
        element = self.mobile_driver.start_activity("com.netflix.mediaclient","o.bWS")
        # # Tap on the element
        element.click()
        #
        actions = ActionChains(self.mobile_driver)
        actions.w3c_actions = ActionBuilder(self.mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(495, 1773)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(532, 1305)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        # self.wait_and_execute(self.mobile_driver, self.download_button_locator, 10, lambda elem: elem.click())
        # self.wait_and_execute(self.mobile_driver, self.hamburger_button, 10, lambda elem: elem.click())
        # self.wait_and_execute(self.mobile_driver, self.tasks_link, 10, lambda elem: elem.click())
        # self.wait_and_execute(self.mobile_driver, self.download_tab, 10, lambda elem: elem.click())
        # dialog_cancel_button_locator = (By)
        # self.logger('pCloud Download started...')
        self.interaction(180)