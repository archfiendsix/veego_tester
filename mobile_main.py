import logging
import subprocess
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

from applications.hideOnline_mobile import HideOnlineMobile
from pages.telemetry import Telemetry
from applications.twitter_mobile import TwitterMobile
from applications.linkedin_mobile import LinkedinMobile
from applications.gmail_mobile import GmailMobile
from applications.instagram_mobile import InstagramMobile
from applications.facebook_mobile import FacebookMobile
from applications.youtube_mobile import YoutubeMobile
from applications.netflix_mobile import NetflixMobile
from applications.tiktok_mobile import TiktokMobile
from applications.twitch_mobile import TwitchMobile
from applications.pcloud_mobile import PCloudMobile
from applications.amazonMusic_mobile import AmazonMusicMobile
from applications.amazonPrime_mobile import AmazonPrimeMobile
from applications.spotify_mobile import SpotifyMobile
from applications.skype_mobile import SkypeMobile
from applications.roblox_mobile import RobloxMobile
from applications.googleMeet_mobile import GoogleMeetMobile
from setup.test_setup import setup_test_environment

# class kill_process_mobile():
#     # logger('clean_computer')
#     # Execute the ADB command to force close the application
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.youtube"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.netflix.mediaclient"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.hitrock.hideonline"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.roblox.client"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.zhiliaoapp.musically"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.twitter.android"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.facebook.katana"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.gm"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.linkedin.android"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.instagram.android"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "tv.twitch.android.app"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.youtube"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.netflix.mediaclient"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.amazon.avod.thirdpartyclient"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.amazon.mp3"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.spotify.music"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.skype.raider"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.google.android.apps.tachyon"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.pcloud.pcloud"])
#     subprocess.run(["adb", "shell", "am", "force-stop", "com.pcloud.pcloud"])
#
#
#
#     os.system(' taskkill /f /im Skype.exe')
#     os.system('taskkill /f /im chrome.exe')
#     os.system('taskkill /f /im WebexMTAV2.exe')
#     os.system('taskkill /f /im WebexHost.exe')
#     os.system('taskkill /f /im wmlhost.exe')
#     os.system('taskkill /f /im atmgr.exe ')
#     os.system('taskkill /f /im CiscoCollabHost.exe')
#     os.system('taskkill /f /im chromedriver.exe')
#     os.system('taskkill /f /im Zoom.exe')
#     os.system('taskkill /f /im Teams.exe')
#     os.system('taskkill /f /im RobloxPlayerBeta.exe')
#     os.system('taskkill /f /im Messenger.exe')
#     os.system('taskkill /f /im steame.exe')
#     os.system('taskkill /f /im steamservice.exe')
#     os.system('taskkill /f /im steamwebhelper.exe')
# #     # logger.info('ending clean_computer')
# #

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
            "newCommandTimeout": 3000,
            # "http" : urllib3.PoolManager(maxsize=10)
        }
        self.mobile_driver = mobile_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
###############################################################################
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
###############################################################################
        # # Load configuration data and test site data from JSON files
        with open(config_dir, "r") as json_file:
            self.config_data = json.load(json_file)
        with open(testsites_dir, "r") as test_sites_json_file:
            self.test_sites_data = json.load(test_sites_json_file)

        # # Initialize page objects
        self.telemetry = Telemetry(self.desktop_driver, self.config_data)
        self.hideOnline_mobile = HideOnlineMobile(self.mobile_driver, self.config_data)

        self.facebook_mobile = FacebookMobile(self.mobile_driver, self.config_data)
        self.gmail_mobile = GmailMobile(self.mobile_driver, self.config_data)
        self.tiktok_mobile = TiktokMobile(self.mobile_driver, self.config_data)
        self.twitter_mobile = TwitterMobile(self.mobile_driver, self.config_data)
        self.twitch_mobile = TwitchMobile(self.mobile_driver, self.config_data)
        self.linkedin_mobile = LinkedinMobile(self.mobile_driver, self.config_data)
        self.instagram_mobile = InstagramMobile(self.mobile_driver, self.config_data)
        self.netflix_mobile = NetflixMobile(self.mobile_driver, self.config_data)
        self.youtube_mobile = YoutubeMobile(self.mobile_driver, self.config_data)
        self.pcloud_mobile = PCloudMobile(self.mobile_driver, self.config_data)
        self.amazonMusic_mobile = AmazonMusicMobile(self.mobile_driver, self.config_data)
        self.amazonPrime_mobile = AmazonPrimeMobile(self.mobile_driver, self.config_data)
        self.spotify_mobile = SpotifyMobile(self.mobile_driver, self.config_data)
        self.skype_mobile = SkypeMobile(self.mobile_driver, self.config_data)
        self.roblox_mobile = RobloxMobile(self.mobile_driver, self.config_data)
        self.googleMeet_mobile = GoogleMeetMobile(self.mobile_driver, self.config_data)
        self.hideOnline_mobile = HideOnlineMobile(self.mobile_driver, self.config_data)
        # self.desktop_driver.maximize_window()

        self.resource = self._get_resource_info( self.config_data, "mobile")

    def _get_resource_info(self, data, tag):
        if isinstance(data, dict):
            if 'tag' in data and data['tag'] == tag:
                return data
            for value in data.values():
                result = self._get_resource_info(value, tag)
                if result:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = self._get_resource_info(item, tag)
                if result:
                    return result
        return None
####################################################################################
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_hideOnline_gaming_mobile(self):
        # kill_process_mobile()
        self.hideOnline_mobile.run_hideOnline_mobile(120)
        self.telemetry.run_telemetry_test('HideOnline', 'GAMING', True, self.hideOnline_mobile.interaction,mac=self.resource['mac'])
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_roblox_gaming_mobile(self):
        # kill_process_mobile()
        self.roblox_mobile.run_roblox_mobile(100)
        self.telemetry.run_telemetry_test('Roblox', 'GAMING', True, self.roblox_mobile.interaction, mac=self.resource['mac'])
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_tiktok_social_mobile(self):
        # kill_process_mobile()
        self.tiktok_mobile.run_tiktok_mobile(70)
        self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True, self.tiktok_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_twitter_social_mobile(self):
        # kill_process_mobile()
        self.twitter_mobile.run_twitter_mobile(100)
        self.telemetry.run_telemetry_test('Twitter', 'SOCIAL', True, self.twitter_mobile.interaction,mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_facebook_social_mobile(self):
        # kill_process_mobile()
        self.facebook_mobile.run_facebook_mobile(80)
        self.telemetry.run_telemetry_test('Facebook', 'SOCIAL', True, self.facebook_mobile.interaction, mac=self.resource.mac)

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_gmail_mail_mobile(self):
        # kill_process_mobile()
        self.gmail_mobile.run_gmail_mobile(30)
        self.telemetry.run_telemetry_test('Gmail', 'MAIL', True, self.gmail_mobile.interaction, mac=self.resource.mac)

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_linkedin_social_mobile(self):
        # kill_process_mobile()
        self.linkedin_mobile.run_linkedin_mobile(30)
        self.telemetry.run_telemetry_test('Linkedin', 'SOCIAL', True, self.linkedin_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_instagram_social_mobile(self):
        # kill_process_mobile()
        self.instagram_mobile.run_instagram_mobile(30)
        self.telemetry.run_telemetry_test('Instagram', 'SOCIAL', True, self.instagram_mobile.interaction, mac=self.resource['mac'])

    # twitch -  WIP
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_twitch_streaming_mobile(self):
        # kill_process_mobile()
        self.twitch_mobile.run_twitch_mobile(30)
        self.telemetry.run_telemetry_test('Twitch', 'STREAMING', True, self.twitch_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_youtube_streaming_mobile(self):
        # kill_process_mobile()
        self.youtube_mobile.run_youtube_mobile(30)
        self.telemetry.run_telemetry_test('Youtube', 'STREAMING', True, self.youtube_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_netflix_streaming_mobile(self):
        # kill_process_mobile()
        self.netflix_mobile.run_netflix_mobile(30)
        self.telemetry.run_telemetry_test('Netflix', 'STREAMING', True, self.netflix_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_amazonPrime_streaming_mobile(self):
        # kill_process_mobile()
        self.amazonPrime_mobile.run_amazonPrime_mobile(30)
        self.telemetry.run_telemetry_test('AmazonPrime', 'STREAMING', True, self.amazonPrime_mobile.interaction, mac=self.resource['mac'])
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_amazonMusic_music_mobile(self):
        # kill_process_mobile()
        self.amazonMusic_mobile.run_amazonMusic_mobile(30)
        self.telemetry.run_telemetry_test('AmazonMusic', 'MUSIC', True, self.amazonMusic_mobile.interaction,mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_spotify_music_mobile(self):
        # kill_process_mobile()
        self.spotify_mobile.run_spotify_mobile(30)
        self.telemetry.run_telemetry_test('Spotify', 'MUSIC', True, self.spotify_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_skype_conferencing_mobile(self):
        # kill_process_mobile()
        self.skype_mobile.run_skype_mobile(120)
        self.telemetry.run_telemetry_test('MSTeams/Skype', 'CONFERENCING', True, self.skype_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_googleMeet_conferencing_mobile(self):
        # kill_process_mobile()
        # self.googleMeet_mobile.run_googleMeet_mobile(45)
        self.telemetry.run_telemetry_test('GoogleMeet', 'CONFERENCING', True, self.googleMeet_mobile.interaction, mac=self.resource['mac'])

    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    def test_pcloud_download_mobile(self):
        # kill_process_mobile()
        self.pcloud_mobile.run_pcloud_download_mobile(120)
        self.telemetry.run_telemetry_test('pcloud', 'DOWNLOAD', True, self.pcloud_mobile.interaction,mac=self.resource['mac'])

    #
    # @pytest.mark.repeat(10)
    # @pytest.mark.sanity
    # def test_pcloud_upload_mobile(self):
    #     self.pcloud_mobile.run_pcloud_upload_mobile(155)
    #     self.telemetry.run_telemetry_test('pcloud', 'UPLOAD', True, self.pcloud_mobile.interaction, mac=self.resource.mac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     )

    def tearDown(self):
        # Close the browser
        self.desktop_driver.quit()
        # self.mobile_driver.quit()


#
# import json
# import os
# import unittest
# from concurrent.futures import ThreadPoolExecutor
#
# from pages.telemetry import Telemetry
# from pages.youtube_page import YoutubePage
# from applications.tiktok_mobile import TiktokMobile
# from setup.test_setup import setup_test_environment
# from appium import webdriver as mobile_webdriver
#
# class TelemetryTest(unittest.TestCase):
#     def setUp(self):
#         # Update paths to be platform-independent
#         download_dir = os.path.abspath(os.path.join(os.getcwd(), "downloads"))
#         config_dir = os.path.abspath(os.path.join(os.getcwd(), "config.json"))
#         torrent_dir = os.path.abspath(os.path.join(os.getcwd(), "fixtures"))
#         testsites_dir = os.path.abspath(os.path.join(os.getcwd(), "fixtures/test_sites.json"))
#
#         # Set Desktop Driver
#         self.desktop_driver = setup_test_environment()
#
#         # Set Mobile Driver
#         desired_caps = {
#             "automationName": "UIAutomator2",
#             "deviceName": "R39M404L59B",
#             "platformName": "Android",
#             "platformVersion": "11",
#             "noReset": True,
#             "newCommandTimeout": 3000
#         }
#         self.mobile_driver = mobile_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
#
#         # Load configuration data and test site data from JSON files
#         with open(config_dir, "r") as json_file:
#             self.config_data = json.load(json_file)
#         with open(testsites_dir, "r") as test_sites_json_file:
#             self.test_sites_data = json.load(test_sites_json_file)
#
#         # Initialize page objects
#         self.youtube_page = YoutubePage(self.desktop_driver, self.test_sites_data)
#         self.tiktok_mobile = TiktokMobile(self.mobile_driver, self.config_data)
#         self.telemetry = Telemetry(self.desktop_driver, self.config_data)
#
#     def test_youtube_tiktok_classification(self):
#         with ThreadPoolExecutor(max_workers=2) as executor:
#             executor.submit(self.run_youtube_tiktok_classification)
#
#     def run_youtube_tiktok_classification(self):
#         self.run_youtube_classification(),
#         self.run_tiktok_classification()
#         self.telemetry.run_telemetry_test('Youtube', 'STREAMING', 'Tiktok', 'SOCIAL', True,
#                                           self.tiktok_mobile.interaction, True, self.youtube_page.interaction)
#
#     def run_youtube_classification(self):
#         self.youtube_page.run_youtube_streaming(100)
#         self.telemetry.run_telemetry_test('Youtube', 'STREAMING', True, self.youtube_page.interaction)
#
#     def run_tiktok_classification(self):
#         self.tiktok_mobile.run_tiktok_mobile(30)
#         self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True, self.tiktok_mobile.interaction)
#
# if __name__ == '__main__':
#     unittest.main()
