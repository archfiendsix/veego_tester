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


class YoutubeMobile(BasePage):
    def __init__(self, mobile_driver, test_sites):
        super().__init__(mobile_driver)
        self.mobile_driver = mobile_driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10


    def interaction(self, timeout):
        # # Get the dimensions of the screen
        # screen_size = self.mobile_driver.get_window_size()
        # width = screen_size['width']
        # height = screen_size['height']
        #
        # start_time = time.time()
        # self.logger('Interacting with TikTok application...')
        # while time.time() - start_time < timeout:
        #     # Wait for a random time between 0 and 5 seconds
        #     time.sleep(random.uniform(0, 5))
        #
        #     # Perform multiple swipe actions
        #     num_swipes = random.randint(2, 3)  # Choose a random number of swipes between 1 and 3
        #     for _ in range(num_swipes):
        #         # Calculate the start and end coordinates for the swipe
        #         start_x = random.uniform(0.2,
        #                                  0.8) * width  # Random start X coordinate within 20%-80% of the screen width
        #         start_y = random.uniform(0.6,
        #                                  0.8) * height  # Random start Y coordinate within 60%-80% of the screen height
        #         end_x = random.uniform(0.2, 0.8) * width  # Random end X coordinate within 20%-80% of the screen width
        #         end_y = random.uniform(0.2, 0.4) * height  # Random end Y coordinate within 20%-40% of the screen height
        #
        #         # Perform the swipe action
        #         action = TouchAction(self.mobile_driver)
        #         action.press(x=start_x, y=start_y).wait(100).move_to(x=end_x, y=end_y).release().perform()
        #     # Pause for a short time before the next set of swipes
        #     time.sleep(1)
        time.sleep(timeout)

    def run_youtube_mobile(self, timeout=30):
        self.logger('Starting Youtube Application...')
        self.mobile_driver.start_activity("com.google.android.youtube","com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity")
        time.sleep(10)
        import subprocess

        # Execute the ADB command to force close the application
        subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.youtube"])

        # actions = ActionChains(self.mobile_driver)
        # actions.w3c_actions.pointer_action.move_to_location(551, 651)
        # actions.click()
        # actions.perform()
        time.sleep(3)
        self.logger('Youtube application started...')
        self.interaction(timeout)

