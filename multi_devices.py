from appium import webdriver as mobile_webdriver
from appium import webdriver
from threading import Thread
from pages.telemetry import Telemetry
from applications.tiktok_mobile import TiktokMobile
from applications.hideOnline_mobile import HideOnlineMobile
from pages.googleMeet_page import GoogleMeetPage
from pages.youtube_page import YoutubePage
import pytest
import json
import os
import unittest
from setup.test_setup import setup_test_environment
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains


class TelemetryTest(unittest.TestCase):
    def setUp(self):
        # Update paths to be platform-independent
        download_dir = os.path.abspath(os.path.join(os.getcwd(), "downloads"))
        config_dir = os.path.abspath(os.path.join(os.getcwd(), "config.json"))
        torrent_dir = os.path.abspath(os.path.join(os.getcwd(), "fixtures"))
        testsites_dir = os.path.abspath(os.path.join(
            os.getcwd(), "fixtures/test_sites.json"))

        # Set driver
        self.driver = setup_test_environment()

        # Set Mobile Driver
        desired_caps = {
            "automationName": "UIAutomator2",
            "deviceName": "R39M404L59B",
            "platformName": "Android",
            "platformVersion": "11",
            "noReset": True,
            "newCommandTimeout": 3000
        }

        self.mobile_driver = mobile_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        # Load configuration data and test site data from JSON files
        with open(config_dir, "r") as json_file:
            self.config_data = json.load(json_file)
        with open(testsites_dir, "r") as test_sites_json_file:
            self.test_sites_data = json.load(test_sites_json_file)

        # Initialize page objects
        self.driver.maximize_window()
        self.telemetry = Telemetry(self.driver, self.config_data)
        self. hideOnline_mobile = HideOnlineMobile(self.driver, self.config_data)
        self.googleMeet_page = GoogleMeetPage(self.driver, self.test_sites_data)
        self.tiktok_mobile = TiktokMobile(self.mobile_driver, self.config_data)
        self.youtube_page = YoutubePage(self.driver, self.test_sites_data)


    def tearDown(self):
        # Close the browser
        self.driver.quit()

    # self.config_data = json.load(json_file)
    # self.driver = setup_test_environment()
    # self.telemetry = Telemetry(self.driver, self.config_data)

    def test_tiktok_youtube_social_streaming_mobile_computer(self):
        tiktok_thread = Thread(target=self.tiktok_mobile.run_tiktok_mobile, args=(180,))
        youtube_thread = Thread(target=self.youtube_page.run_youtube_streaming, args=(180,))

        tiktok_thread.start()
        youtube_thread.start()

        # wait for both threads to finish
        tiktok_thread.join(timeout=60)
        youtube_thread.join(timeout=60)
        if tiktok_thread.is_alive():
            pass
            # something went wrong the thread is still running
        if youtube_thread.is_alive():
            pass
            # something went wrong the thread is still running

        # test was over

        self.telemetry.run_telemetry_test(
            service_name='Tiktok', service_type='SOCIAL', classification_final=True,
            interaction=self.tiktok_mobile.interaction, mac="a8:db:03:b2:78:13")
        # self.windows_resource['mac']

        self.telemetry.run_telemetry_test(
            service_name='Youtube', service_type='STREAMING', classification_final=True,
            interaction=self.youtube_page.interaction, mac="14:ab:c5:01:8e:6b")
        # self.mobile_resource['mac']

    def test_hideOnline_googleMeet_gaming_conference_mobile_computer(self):
        hideOnline_thread = Thread(target=self.hideOnline_mobile.run_hideOnline_mobile, args=(180,))
        googleMeet_thread = Thread(target=self.googleMeet_page.run_googleMeet_conference, args=(180,))

        hideOnline_thread.start()
        googleMeet_thread.start()

        # wait for both threads to finish
        hideOnline_thread.join(timeout=60)
        googleMeet_thread.join(timeout=60)
        if  hideOnline_thread.is_alive():
            pass
            # something went wrong the thread is still running
        if googleMeet_thread.is_alive():
            pass
            # something went wrong the thread is still running

        # test was over

        self.telemetry.run_telemetry_test(
            service_name='HideOnline', service_type='GAMING', classification_final=True,
            interaction=self.hideOnline_mobile.interaction, mac="a8:db:03:b2:78:13")
        # self.windows_resource['mac']

        self.telemetry.run_telemetry_test(
            service_name='GoogleMeet', service_type='CONFERENCING', classification_final=True,
            interaction=self.googleMeet_page.interaction, mac="14:ab:c5:01:8e:6b")


    # def test_hideOnline_gaming_mobile(self):
    #     # kill_process_mobile()
    #     self.hideOnline_mobile.run_hideOnline_mobile(120)
    #     self.telemetry.run_telemetry_test('HideOnline', 'GAMING', True, self.hideOnline_mobile.interaction, mac=self.resource.mac)
    # def test_GoogleMeet_conference(self):
    #
    #     self.googleMeet_page.run_googleMeet_conference(130)
    #     self.telemetry.run_telemetry_test('GoogleMeet', 'CONFERENCING', True, self.googleMeet_page.interaction,
    #                                       mac=self.resource['mac'])