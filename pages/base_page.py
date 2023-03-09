import logging
import pickle
import random
import time
import threading
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

load_dotenv()
class BasePage:
    def __init__(self, driver):
        self.driver = driver,
        self.timeout = 10


        # Set environment variables
        self.env_username = os.getenv("VEEGO_USERNAME")
        self.env_password = os.getenv("VEEGO_PASSWORD")
        self.env_soundcloud_email = os.getenv("SOUNDCLOUD_EMAIL")
        self.env_soundcloud_password = os.getenv("SOUNDCLOUD_PASSWORD")
        self.env_twitter_email = os.getenv("TWITTER_EMAIL")
        self.env_twitter_password = os.getenv("TWITTER_PASSWORD")
        self.env_nexusmods_email = os.getenv("NEXUSMODS_EMAIL")
        self.env_nexusmods_password = os.getenv("NEXUSMODS_PASSWORD")
        self.env_icloud_email = os.getenv("ICLOUD_EMAIL")
        self.env_icloud_password = os.getenv("ICLOUD_PASSWORD")
        self.env_tiktok_username = os.getenv("TIKTOK_USERNAME")
        self.env_tiktok_password = os.getenv("TIKTOK_PASSWORD")
        self.env_messenger_email = os.getenv("MESSENGER_EMAIL")
        self.env_messenger_password = os.getenv("MESSENGER_PASSWORD")
        self.env_facebook_email = os.getenv("FACEBOOK_EMAIL")
        self.env_facebook_password = os.getenv("FACEBOOK_PASSWORD")
    def dump_cookies(self):
        # with open("fixtures/cookies.pkl", "wb") as f:
        #     pickle.dump(self.driver.get_cookies(), f)
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open("fixtures/cookies.pkl", "wb"))

    def load_cookies(self):
        with open("fixtures/cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    def try_interaction_thread(self):
        print("Interacting with page...\n")
        # define a function to do the scrolling
        def scroll_function(driver):
            scroll_direction = "down"
            while True:
                if scroll_direction == "down":
                    scroll_amount = random.randint(300, 1000)
                    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                else:
                    scroll_amount = random.randint(300, 1000)
                    driver.execute_script(f"window.scrollBy(0, -{scroll_amount});")
                time.sleep(random.randint(0, 1))  # wait for n seconds between scrolls
                if scroll_direction == "down" and driver.execute_script(
                        "return window.innerHeight + window.pageYOffset") >= driver.execute_script(
                        "return document.body.scrollHeight"):
                    scroll_direction = "up"
                elif scroll_direction == "up" and driver.execute_script("return window.pageYOffset") == 0:
                    scroll_direction = "down"

        # define a function to do the button click
        def click_function(driver):
            while True:
                try:
                    time.sleep(random.randint(0, 60))
                    soundcloud_skip_button_locator = (By.CSS_SELECTOR, ".skipControl__next")
                    self.wait_and_execute(driver, soundcloud_skip_button_locator, 10, lambda elem: elem.click())
                except (NoSuchElementException, TimeoutException):
                    pass

        # start the two threads
        scroll_thread = threading.Thread(target=scroll_function, args=(self.driver,))
        click_thread = threading.Thread(target=click_function, args=(self.driver,))
        scroll_thread.start()
        click_thread.start()

        # join the threads to wait for them to finish (optional)
        scroll_thread.join()

    def timout_while_interact(self, timeout):
        print("Interacting with page...")
        start_time = time.time()
        scroll_direction = 'down'
        while time.time() - start_time < timeout:

            if scroll_direction == "down":
                scroll_amount = random.randint(500, 1000)
                self.driver.execute_script(
                    f"window.scrollBy(0, {scroll_amount});")
            else:
                scroll_amount = random.randint(500, 1000)
                self.driver.execute_script(
                    f"window.scrollBy(0, -{scroll_amount});")
            # time.sleep(random.randint(0, 1))  # wait for n seconds between scrolls
            if scroll_direction == "down" and self.driver.execute_script(
                    "return window.innerHeight + window.pageYOffset") >= self.driver.execute_script(
                    "return document.body.scrollHeight"):
                scroll_direction = "up"
            elif scroll_direction == "up" and self.driver.execute_script("return window.pageYOffset") == 0:
                scroll_direction = "down"

            #Control for Soundcloud Music
            try:
                time.sleep(random.randint(1, 3))
                soundcloud_skip_button_locator = (By.CSS_SELECTOR, ".skipControl__next")
                self.wait_and_execute(self.driver, soundcloud_skip_button_locator, 10, lambda elem: elem.click())
            except (NoSuchElementException, TimeoutException):
                pass



    def wait_and_execute(self, driver, locator, timeout, action):
        time.sleep(random.randint(1, 2))

        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator))
        action(element)


    def logger(self, text):
        logging.info(text)
