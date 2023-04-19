import json
import os
import unittest
import random
import json
import time
import os
import pytest
import urllib3
from appium import webdriver as mobile_webdriver
from selenium.webdriver.chrome.options import Options
from appium.webdriver import Remote
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerInput
from selenium.webdriver.common.by import By
from pages.telemetry import Telemetry
from applications.linkedin_mobile import LinkedinMobile
from applications.instagram_mobile import InstagramMobile
from applications.facebook_mobile import FacebookMobile
from applications.youtube_mobile import YoutubeMobile
from applications.netflix_mobile import NetflixMobile
from applications.tiktok_mobile import TiktokMobile
from applications.twitch_mobile import TwitchMobile
from applications.pcloud_mobile import PCloudMobile
from setup.test_setup import setup_test_environment




class TelemetryTest(unittest.TestCase):
    def setUp(self):
        # Update paths to be platform-independent
        download_dir = os.path.abspath(os.path.join(os.getcwd(), "downloads"))
        config_dir = os.path.abspath(os.path.join(os.getcwd(), "config.json"))
        torrent_dir = os.path.abspath(os.path.join(os.getcwd(), "fixtures"))
        testsites_dir = os.path.abspath(os.path.join(
            os.getcwd(), "fixtures/test_sites.json"))

        # Set Desktop Driver
        self.desktop_driver = setup_test_environment()

        # Set Mobile Driver
        desired_caps = {
            "automationName": "UIAutomator2",
            "deviceName": "R39M404L59B",
            "platformName": "Android",
            "platformVersion": "11",
            "noReset": True,
            "newCommandTimeout": 120
        }

        self.mobile_driver = mobile_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        # # Load configuration data and test site data from JSON files
        with open(config_dir, "r") as json_file:
            self.config_data = json.load(json_file)
        with open(testsites_dir, "r") as test_sites_json_file:
            self.test_sites_data = json.load(test_sites_json_file)

        # # Initialize page objects
        self.telemetry = Telemetry(self.desktop_driver, self.config_data)
        self.facebook_mobile = FacebookMobile(self.mobile_driver, self.config_data)
        self.tiktok_mobile = TiktokMobile(self.mobile_driver, self.config_data)
        self.twitch_mobile = TwitchMobile(self.mobile_driver, self.config_data)
        self.linkedin_mobile = LinkedinMobile(self.mobile_driver, self.config_data)
        self.instagram_mobile = InstagramMobile(self.mobile_driver, self.config_data)
        self.netflix_mobile = NetflixMobile(self.mobile_driver, self.config_data)
        self.youtube_mobile = YoutubeMobile(self.mobile_driver, self.config_data)
        self.pcloud_mobile = PCloudMobile(self.mobile_driver, self.config_data)
        self.desktop_driver.maximize_window()

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_tiktok_social_mobile(self):
        self.tiktok_mobile.run_tiktok_mobile(30)
        self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True, self.tiktok_mobile.interaction)
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_facebook_social_mobile(self):
        self.facebook_mobile.run_facebook_mobile(30)
        self.telemetry.run_telemetry_test('Facebook', 'SOCIAL', True, self.facebook_mobile.interaction)

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_linkedin_social_mobile(self):
        self.linkedin_mobile.run_linkedin_mobile(30)
        self.telemetry.run_telemetry_test('Linkedin', 'SOCIAL', True, self.linkedin_mobile.interaction)

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_instagram_social_mobile(self):
        self.instagram_mobile.run_instagram_mobile(30)
        self.telemetry.run_telemetry_test('Instagram', 'SOCIAL', True, self.instagram_mobile.interaction)
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_twitch_streaming_mobile(self):
        self.twitch_mobile.run_twitch_mobile(30)
        self.telemetry.run_telemetry_test('Twitch', 'STREAMING', True, self.twitch_mobile.interaction)
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_youtube_streaming_mobile(self):
        self.youtube_mobile.run_youtube_mobile(30)
        self.telemetry.run_telemetry_test('Youtube', 'STREAMING', True, self.youtube_mobile.interaction)
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_netflix_streaming_mobile(self):
        self.netflix_mobile.run_netflix_mobile(30)
        self.telemetry.run_telemetry_test('Netflix', 'STREAMING', True, self.netflix_mobile.interaction)
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_pcloud_download_mobile(self):
        self.pcloud_mobile.run_pcloud_download_mobile(155)
        self.telemetry.run_telemetry_test('pcloud', 'DOWNLOAD', True, self.pcloud_mobile.interaction)

    #
    # @pytest.mark.repeat(10)
    # @pytest.mark.sanity
    # def test_pcloud_upload_mobile(self):
    #     self.pcloud_mobile.run_pcloud_upload_mobile(155)
    #     self.telemetry.run_telemetry_test('pcloud', 'UPLOAD', True, self.pcloud_mobile.interaction)

    def tearDown(self):
        # Close the browser
        self.desktop_driver.quit()
        # self.mobile_driver.quit()
