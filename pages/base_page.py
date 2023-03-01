import logging
import urllib3
import pickle
import random
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains

import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver,
        self.timeout = 10

        # Set the path to the .env file based on the current operating system
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')

        # Load environment variables from the .env file
        load_dotenv(env_file)

        # Set environment variables
        self.env_username = os.getenv("USERNAME")
        self.env_password = os.getenv("PASSWORD")
        self.env_soundcloud_email = os.getenv("SOUNDCLOUD_EMAIL")
        self.env_soundcloud_password = os.getenv("SOUNDCLOUD_PASSWORD")
        self.env_twitter_email = os.getenv("TWITTER_EMAIL")
        self.env_twitter_password = os.getenv("TWITTER_PASSWORD")
        self.env_nexusmods_email = os.getenv("NEXUSMODS_EMAIL")
        self.env_nexusmods_password = os.getenv("NEXUSMODS_PASSWORD")
        self.env_icloud_email = os.getenv("ICLOUD_EMAIL")
        self.env_icloud_password = os.getenv("ICLOUD_PASSWORD")

    def setup(self):
        pass

    def maximize_window(self):
        self.driver.maximize_window()

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

    def random_scroll(self):
        # Set the time limit for scrolling
        time_limit = 3.5  # seconds

        # Set the initial scrolling direction to "down"
        scroll_direction = "down"

        # Scroll the page alternately up and down by random amounts for 3.5 seconds
        start_time = time.time()
        while time.time() - start_time < time_limit:
            scroll_amount = random.randint(500, 1000)
            if scroll_direction == "down":
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            else:
                self.driver.execute_script(f"window.scrollBy(0, -{scroll_amount});")
            time.sleep(0.5)  # wait for 0.5 seconds between scrolls
            if scroll_direction == "down" and self.driver.execute_script("return window.innerHeight + window.pageYOffset") >= self.driver.execute_script("return document.body.scrollHeight"):
                scroll_direction = "up"
            elif scroll_direction == "up" and self.driver.execute_script("return window.pageYOffset") == 0:
                scroll_direction = "down"
    def timout_while_interact(self,timeout):
        start_time = time.time()
        while time.time() - start_time < timeout:
            self.random_scroll()


    def logger(self, text):
        logging.info(text)
