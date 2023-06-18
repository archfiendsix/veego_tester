import time
import os
import random

from appium.webdriver.common.mobileby import MobileBy
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


class HideOnlineMobile(BasePage):
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
        # self.logger('Interacting with HideOnline application...')
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
        # time.sleep(timeout)

        # Get the dimensions of the screen
        screen_size = self.mobile_driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        start_time = time.time()
        self.logger('Interacting with HideOnline application...')
        while time.time() - start_time < timeout:
            # Wait for a random time between 0 and 5 seconds
            time.sleep(random.uniform(0, 5))

            # Perform multiple swipe actions
            num_swipes = random.randint(2, 3)  # Choose a random number of swipes between 1 and 3
            for _ in range(num_swipes):
                # Calculate the start and end coordinates for the swipe
                start_x = random.uniform(0.2,
                                         0.8) * width  # Random start X coordinate within 20%-80% of the screen width
                start_y = random.uniform(0.6,
                                         0.8) * height  # Random start Y coordinate within 60%-80% of the screen height
                end_x = random.uniform(0.2, 0.8) * width  # Random end X coordinate within 20%-80% of the screen width
                end_y = random.uniform(0.2, 0.4) * height  # Random end Y coordinate within 20%-40% of the screen height

                # Perform the swipe action
                action = TouchAction(self.mobile_driver)
                action.press(x=start_x, y=start_y).wait(100).move_to(x=end_x, y=end_y).release().perform()

            # Pause for a short time before the next set of swipes
            time.sleep(1)
        ##########

        time.sleep(timeout)


    def run_hideOnline_mobile(self, timeout=30):
        self.logger('Starting HideOnline Application...')
        time.sleep(3)
        self.mobile_driver.start_activity("com.hitrock.hideonline", "com.unity3d.player.UnityPlayerActivity")
        time.sleep(14)

        # Get the dimensions of the screen
        screen_width = self.mobile_driver.get_window_size()['width']
        screen_height = self.mobile_driver.get_window_size()['height']
        time.sleep(15)

        # Calculate the coordinates to tap on the screen
        x = 388  # X-coordinate of the tap
        y = 985  # Y-coordinate of the tap

        # Perform the tap action
        action = TouchAction(self.mobile_driver)
        action.tap(x=x, y=y).perform()
        time.sleep(10)
        # Calculate the coordinates to tap on the screen
        x = 530  # X-coordinate of the tap
        y = 860  # Y-coordinate of the tap

        # Perform the tap action
        action = TouchAction(self.mobile_driver)
        action.tap(x=x, y=y).perform()
        time.sleep(15)
        # Calculate the coordinates to tap on the screen
        x = 530  # X-coordinate of the tap
        y = 860  # Y-coordinate of the tap

        # Perform the tap action
        action = TouchAction(self.mobile_driver)
        action.tap(x=x, y=y).perform()
        # ############################
        # # Switch to the new window
        # window_handles = self.mobile_driver.window_handles
        # self.mobile_driver.switch_to.window(window_handles[-1])
        #
        # # Perform the click action in the new window
        # actions = ActionChains(self.mobile_driver)
        # actions.click().perform()
        # #time.sleep(7)
        # Find the element using XPath
        # button_xpath = " //*[@id='screenshotContainer']/div[2]/div/div/div/div/div[18]/div"
        #
        # # Perform the tap action on the element
        # button_element = self.mobile_driver.find_element(MobileBy.XPATH, button_xpath)
        # action = TouchAction(self.mobile_driver)
        # action.tap(element=button_element).perform()

        # element = self.mobile_driver.find_element_by_id("com.roblox.client:id/inset_layout_bottom")
        # element.click()

        time.sleep(2)

        self.logger('HideOnline application started...')

        self.interaction(timeout)