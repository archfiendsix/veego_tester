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
from applications.tiktok_mobile import TiktokMobile
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
            "deviceName": "477cffc9",
            "platformName": "Android",
            "platformVersion": "13",
            "noReset": True
        }

        self.mobile_driver = mobile_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        # Load configuration data and test site data from JSON files
        with open(config_dir, "r") as json_file:
            self.config_data = json.load(json_file)
        with open(testsites_dir, "r") as test_sites_json_file:
            self.test_sites_data = json.load(test_sites_json_file)

        # Initialize page objects
        self.telemetry = Telemetry(self.desktop_driver, self.config_data)
        self.tiktok_mobile = TiktokMobile(self.mobile_driver, self.config_data)
        self.pcloud_mobile = PCloudMobile(self.mobile_driver, self.config_data)
        self.desktop_driver.maximize_window()

    @pytest.mark.repeat(10)
    @pytest.mark.sanity
    def test_tiktok_social_mobile(self):
        self.tiktok_mobile.run_tiktok_mobile(155)
        self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True, self.tiktok_mobile.interaction)

    @pytest.mark.repeat(10)
    @pytest.mark.sanity
    def test_pcloud_download_mobile(self):
        self.pcloud_mobile.run_pcloud_download_mobile(155)
        self.telemetry.run_telemetry_test('pcloud', 'DOWNLOAD', True, self.pcloud_mobile.interaction)

    @pytest.mark.repeat(10)
    @pytest.mark.sanity
    def test_pcloud_upload_mobile(self):
        self.pcloud_mobile.run_pcloud_upload_mobile(155)
        self.telemetry.run_telemetry_test('pcloud', 'UPLOAD', True, self.pcloud_mobile.interaction)

    def tearDown(self):
        # Close the browser
        self.desktop_driver.quit()
        self.mobile_driver.quit()
