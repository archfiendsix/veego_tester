from appium import webdriver as mobile_webdriver
from appium import webdriver
import time
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
import subprocess
import urllib3
from setup.test_setup import setup_test_environment
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains


class kill_process_mobile():
    # logger('clean_computer')
    # Execute the ADB command to force close the application
    subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.youtube"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.netflix.mediaclient"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.hitrock.hideonline"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.roblox.client"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.zhiliaoapp.musically"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.twitter.android"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.facebook.katana"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.gm"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.linkedin.android"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.instagram.android"])
    subprocess.run(["adb", "shell", "am", "force-stop", "tv.twitch.android.app"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.youtube"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.netflix.mediaclient"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.amazon.avod.thirdpartyclient"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.amazon.mp3"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.spotify.music"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.skype.raider"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.apps.tachyon"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.pcloud.pcloud"])
    subprocess.run(["adb", "shell", "am", "force-stop", "com.pcloud.pcloud"])



    os.system(' taskkill /f /im Skype.exe')
    os.system('taskkill /f /im chrome.exe')
    os.system('taskkill /f /im WebexMTAV2.exe')
    os.system('taskkill /f /im WebexHost.exe')
    os.system('taskkill /f /im wmlhost.exe')
    os.system('taskkill /f /im atmgr.exe ')
    os.system('taskkill /f /im CiscoCollabHost.exe')
    os.system('taskkill /f /im chromedriver.exe')
    os.system('taskkill /f /im Zoom.exe')
    os.system('taskkill /f /im Teams.exe')
    os.system('taskkill /f /im RobloxPlayerBeta.exe')
    os.system('taskkill /f /im Messenger.exe')
    os.system('taskkill /f /im steame.exe')
    os.system('taskkill /f /im steamservice.exe')
    os.system('taskkill /f /im steamwebhelper.exe')
#     # logger.info('ending clean_computer')
#


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
        # # Create a custom connection pool with an increased size
        # http = urllib3.PoolManager(num_pools=10)
        #
        # # Make the request using the updated connection pool
        # response = http.request('GET', 'http://localhost')
        # # Access the response data
        # data = response.data
        # status_code = response.status
        #
        # # Use the response data in your code
        # if status_code == 200:
        #     # Process the data
        #     print(data)
        # else:
        #     # Handle the error or unexpected status code
        #     print("Request failed with status code:", status_code)

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
        tiktok_thread = Thread(target=self.tiktok_mobile.run_tiktok_mobile, args=(60,))
        youtube_thread = Thread(target=self.youtube_page.run_youtube_streaming, args=(60,))

        tiktok_thread.start()
        youtube_thread.start()

        # wait for both threads to finish
        tiktok_thread.join(timeout=40)
        youtube_thread.join(timeout=40)
        if tiktok_thread.is_alive():
            pass
            # something went wrong the thread is still running
        if youtube_thread.is_alive():
            pass
            # something went wrong the thread is still running

        # test was over

        self.telemetry.run_telemetry_test(
            service_name='Tiktok', service_type='SOCIAL', classification_final=True,
            interaction=self.tiktok_mobile.interaction, mac="fa:8a:27:b3:a5:53")
        # self.windows_resource['mac']

        self.telemetry.run_telemetry_test(
            service_name='Youtube', service_type='STREAMING', classification_final=True,
            interaction=self.youtube_page.interaction, mac="14:ab:c5:01:8e:6b")
        # self.mobile_resource['mac']

    def test_hideOnline_googleMeet_gaming_conference_mobile_computer(self):
        hideOnline_thread = Thread(target=self.hideOnline_mobile.run_hideOnline_mobile, args=(80,))

        googleMeet_thread = Thread(target=self.googleMeet_page.run_googleMeet_conference, args=(80,))

        hideOnline_thread.start()
        googleMeet_thread.start()

        # wait for both threads to finish
        hideOnline_thread.join(timeout=40)
        googleMeet_thread.join(timeout=40)
        if  hideOnline_thread.is_alive():
            pass
            # something went wrong the thread is still running
        if googleMeet_thread.is_alive():
            pass
            # something went wrong the thread is still running

        # test was over

        self.telemetry.run_telemetry_test(
            service_name='HideOnline', service_type='GAMING', classification_final=True,
            interaction=self.hideOnline_mobile.interaction, mac="2a:e3:33:cd:10:5b")
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