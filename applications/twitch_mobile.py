import time
import os
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


class TwitchMobile(BasePage):
    def __init__(self, mobile_driver, test_sites):
        super().__init__(mobile_driver)
        self.mobile_driver = mobile_driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        # #timeout = 30  # Set the desired timeout in seconds
        #
        # # Get the dimensions of the screen
        # screen_size = self.mobile_driver.get_window_size()
        # width = screen_size['width']
        # height = screen_size['height']
        #
        # start_time = time.time()
        # self.logger('Interacting with Youtube application...')
        # while time.time() - start_time < timeout:
        #     # Wait for a random time between 0 and 5 seconds
        #     time.sleep(random.uniform(0, 5))
        #
        #     # Perform multiple swipe actions
        #     num_swipes = random.randint(2, 3)  # Choose a random number of swipes between 1 and 3
        #     for _ in range(num_swipes):
        #         # Calculate the start and end coordinates for the swipe
        #         start_x = random.uniform(0.6, 0.8) * width  # Random start X coordinate within 60%-80% of the screen width
        #         start_y = random.uniform(0.6, 0.8) * height  # Random start Y coordinate within 60%-80% of the screen height
        #         end_x = random.uniform(0.8, 0.9) * width  # Random end X coordinate within 80%-90% of the screen width
        #         end_y = random.uniform(0.6, 0.8) * height  # Random end Y coordinate within 60%-80% of the screen height
        #
        #         # Perform the swipe action
        #         action = TouchAction(self.mobile_driver)
        #         action.press(x=start_x, y=start_y).wait(100).move_to(x=end_x, y=end_y).release().perform()
        #
        #     # Pause for a short time before the next set of swipes
        #     time.sleep(1)

        time.sleep(timeout)


    def run_twitch_mobile(self, timeout=20):
        self.logger('Starting Twitch Application...')
        self.mobile_driver.start_activity("tv.twitch.android.app", ".core.LandingActivity")
        self.mobile_driver.quit()
        # Wait for the Twitch application to fully load
        time.sleep(5)  # Adjust the delay based on the application's loading time

        # Perform sliding action for a specific duration
        duration = 5  # Set the desired duration in seconds

        # Get the dimensions of the screen
        screen_size = self.mobile_driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        # Calculate the start and end coordinates for the slide
        start_x = width // 2  # Start X coordinate at the center of the screen
        start_y = height // 3  # Start Y coordinate at 1/3rd position from the top of the screen
        end_x = width // 2  # End X coordinate at the center of the screen
        end_y = height // 3 * 2  # End Y coordinate at 2/3rd position from the top of the screen

        # Calculate the duration for each step of the slide
        step_duration = 0.1  # Set the desired duration for each step in seconds
        num_steps = int(duration / step_duration)  # Calculate the number of steps

        # Perform the press action
        action = TouchAction(self.mobile_driver)
        action.press(x=start_x, y=start_y).wait(100).release().perform()

        # Perform the continuous move_to action
        for _ in range(num_steps):
            # Calculate the intermediate coordinates for each step of the slide
            intermediate_y = start_y + (end_y - start_y) / num_steps * (_ + 1)

            # Perform the move_to action for each step
            action = TouchAction(self.mobile_driver)
            action.move_to(x=end_x, y=intermediate_y).wait(int(step_duration * 1000)).perform()

        # Pause for a short time before exiting
        time.sleep(1)

        # self.logger('Starting Twitch Application...')
        # self.mobile_driver.start_activity("tv.twitch.android.app",".core.LandingActivity")
        # time.sleep(15)
        # actions = ActionChains(self.mobile_driver)
        # actions.w3c_actions.pointer_action.move_to_location(408, 2024)
        # actions.click()
        # actions.perform()
        # time.sleep(3)e","name":"long-clickable"},{"key":"password","value":"false","false","name":"selected"},{"key":"bounds","value":"[48,635][348,1035]","name":"bounds"},{"key":"displayed","value":"true","name":"displayed"}]')
        # element.click()
        # time.sleep(3)

        # //*[@id="screenshotContainer"]/div[2]/div/div/div/div/div[45]
        # actions = ActionChains(self.mobile_driver)
        # actions.w3c_actions = ActionBuilder(self.mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(200, 850)
        # time.sleep(1)
        # self.wait_and_execute(self.mobile_driver, self.download_button_locator, 10, lambda elem: elem.click())
        # actions.click()
        # time.sleep(1)
        # actions.perform()
        # time.sleep(2)
        # element = self.mobile_driver.find_element(By.ID, 'tv.twitch.android.app:id/viewers')
        # element = self.mobile_driver.find_element(By.ID, TWITCH_PLAY_VIDEO_LIVE)
        # time.sleep(1)
        # element.click()
        self.logger('Twitch application started...')
        self.interaction(timeout)