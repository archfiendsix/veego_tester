
import json
import logging
import os
import unittest
import urllib3
import pathlib
import pickle
import re
from playwright.sync_api import Page, expect
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as webdriver
# from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from pages.microsoft_page import MicrosoftPage
from pages.messenger_page import MessengerPage
from pages.nexusmods_page import NexusModsPage
from pages.soundcloud_page import SoundcloudPage
from pages.telemetry import Telemetry
from pages.twitter_page import TwitterPage
from pages.tiktok_page import TiktokPage
from pages.youtube_page import YoutubePage
from pages.icloud_page import IcloudPage
from pages.tiktok_page import TiktokPage

class TelemetryTest(unittest.TestCase):
    def setUp(self):
        # Load environment variables from .env file
        load_dotenv()

        # Initialize the Chrome driver
        chrome_driver_path = "./drivers/chromedriver"
        driver_service = ChromeDriverManager().install()
        download_dir = os.path.join(os.getcwd(), "downloads")
        chrome_options = webdriver.ChromeOptions()

        prefs = {"download.default_directory": download_dir}
        chrome_options.add_experimental_option("prefs", prefs)
        sessions_dir = os.path.join(os.getcwd(), "sessions")
        chrome_options.add_argument(f"--user-data-dir={sessions_dir}")
        chrome_options.add_argument('--no-sandbox')
        # driver_service = webdriver.chrome.service.Service(
        #     ChromeDriverManager().install())

        # self.driver = webdriver.Chrome(service=driver_service,
        #                                executable_path=chrome_driver_path, options=chrome_options
        #                                )
        
        self.driver = webdriver.Chrome(options=chrome_options
                                    )
     

        # Disable SSL warnings and set up logging
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s : %(message)s",
            handlers=[logging.StreamHandler()],
        )
        logging.getLogger().setLevel(logging.INFO)

        # Load configuration data and test site data from JSON files
        config_dir = os.path.join(os.getcwd(), "config.json")
        with open(config_dir, "r") as json_file:
            self.config_data = json.load(json_file)
        testsites_dir = os.path.join(os.getcwd(), "fixtures/test_sites.json")
        with open(testsites_dir, "r") as test_sites_json_file:
            self.test_sites_data = json.load(test_sites_json_file)

        # Initialize page objects
        self.youtube_page = YoutubePage(self.driver, self.test_sites_data)
        self.telemetry = Telemetry(self.driver, self.config_data)
        self.messenger_page = MessengerPage(self.driver)
        self.soundcloud_page = SoundcloudPage(
            self.driver, self.test_sites_data)
        self.twitter_page = TwitterPage(self.driver, self.test_sites_data)
        self.nexusmods_page = NexusModsPage(self.driver, self.test_sites_data)
        self.microsoft_page = MicrosoftPage(self.driver, self.test_sites_data)
        self.icloud_page = IcloudPage(self.driver, self.test_sites_data)
        self.tiktok_page = TiktokPage(self.driver, self.test_sites_data)

    def test_youtube_streaming(self):
        self.youtube_page.run_youtube_streaming(180)
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('Youtube', 'STREAMING', True)

    def test_youtube_download(self):
        self.youtube_page.run_youtube_download(180)
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('Youtube', 'DOWNLOAD', True)

    def test_twitter_social(self):
        # Open Twitter Social (DONE - runner, checker)
        self.twitter_page.run_twitter()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('Twitter', 'SOCIAL', True)
    
    def test_tiktok_social(self):
        # Open Tiktok Social (DONE - runner, checker)
        self.tiktok_page.run_tiktok()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True)

    def test_messenger_conference(self):
        # Open a messenger conference (not done)
        self.messenger_page.run_messenger_conference()

    def test_soundcloud_music(self):
        #play a soundcloud music (DONE - runner, checker)
        self.soundcloud_page.run_soundcloud_music()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('SoundCloud', 'MUSIC', True)

    def test_soundcloud_upload(self): #Can't run this. it needs subscription to upload/download more files
        # Execute soundcloud upload (done)
        self.soundcloud_page.run_soundcloud_upload()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('SoundCloud', 'UPLOAD', True)

    def test_microsoft_download(self):
        # Test downloading a file from Microsoft's website (DONE - runner, checker - But no services shows on api)
        self.microsoft_page.run_microsoft_download()

        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('Microsoft', 'DOWNLOAD', True)

    def test_nexusmods_download(self):
        # Test downloading a file from Nexus Mods
        self.nexusmods_page.run_nexusmods_download()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('NexusMods', 'DOWNLOAD', True)

    def test_icloud_download(self): #Can't run this. it needs subscription to upload/download more files
        # Test downloading a file from iCloud
        self.icloud_page.run_icloud_download()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('Microsoft', 'DOWNLOAD', True)

    def test_icloud_upload(self): #Can't run this. it needs subscription to upload/download more files
        # Test uploading a file to iCloud
        self.icloud_page.run_icloud_upload()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test('iCloud', 'UPLOAD', True)

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    # Run the test case
    unittest.main()
