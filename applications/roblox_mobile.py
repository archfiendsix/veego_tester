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


class RobloxMobile(BasePage):
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
        # self.logger('Roblox with Instagram application...')
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


    def run_roblox_mobile(self, timeout=50):
        self.logger('Starting Roblox Application...')
        self.mobile_driver.start_activity("com.roblox.client", "startup.ActivitySplash")
        time.sleep(4)

        # # Get the dimensions of the screen
        screen_width = self.mobile_driver.get_window_size()['width']
        screen_height = self.mobile_driver.get_window_size()['height']
        time.sleep(3)

        # Calculate the coordinates to tap on the screen
        x = 200  # X-coordinate of the tap
        y = 1351  # Y-coordinate of the tap

        # Perform the tap action
        action = TouchAction(self.mobile_driver)
        action.tap(x=x, y=y).perform()
        time.sleep(3)
        # Calculate the coordinates to tap on the screen
        x = 542  # X-coordinate of the tap
        y = 1919  # Y-coordinate of the tap

        # Perform the tap action
        action = TouchAction(self.mobile_driver)
        action.tap(x=x, y=y).perform()
        time.sleep(3)
        # Calculate the coordinates to tap on the screen
        x = 538  # X-coordinate of the tap
        y = 858  # Y-coordinate of the tap

        # Perform the tap action
        action = TouchAction(self.mobile_driver)
        action.tap(x=x, y=y).perform()

        time.sleep(15)
        # Calculate the coordinates to tap on the screen
        x = 676  # X-coordinate of the tap
        y = 2041  # Y-coordinate of the tap

        # Perform the tap action
        action = TouchAction(self.mobile_driver)
        action.tap(x=x, y=y).perform()
        action = TouchAction(self.mobile_driver)
        action.click()
        action.click()
        time.sleep(2)

        # button_xpath = "//android.widget.FrameLayout[@resource-id='com.roblox.client:id/inset_layout_bottom']//android.widget.Button"
        # button = self.mobile_driver.find_element_by_xpath(button_xpath)
        # button.click()
        # # Switch to the new window
        # window_handles = self.mobile_driver.window_handles
        # self.mobile_driver.switch_to.window(window_handles[-1])
        #
        # # Perform the click action in the new window
        # actions = ActionChains(self.mobile_driver)
        # actions.click().perform()
        time.sleep(7)
        # Find the element using XPath
        # button_xpath = " //*[@id='screenshotContainer']/div[2]/div/div/div/div/div[18]/div"
        #
        # # Perform the tap action on the element
        # button_element = self.mobile_driver.find_element(MobileBy.XPATH, button_xpath)
        # action = TouchAction(self.mobile_driver)
        # action.tap(element=button_element).perform()
        # element.click()
        # element = self.mobile_driver.find_element_by_id("com.pcloud.pcloud:id/action_download")
        # element.click()

        time.sleep(2)

        self.logger('Roblox application started...')

        self.interaction(timeout)