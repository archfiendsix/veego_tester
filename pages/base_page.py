import logging
import urllib3
import pickle
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

    def logger(self, text):
        logging.info(text)
