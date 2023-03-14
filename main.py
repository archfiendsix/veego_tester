import json
import os
import unittest
from setup.test_setup import setup_test_environment
from pages.microsoft_page import MicrosoftPage
from pages.messenger_page import MessengerPage
from pages.nexusmods_page import NexusModsPage
from pages.soundcloud_page import SoundcloudPage
from pages.telemetry import Telemetry
from pages.twitter_page import TwitterPage
from pages.youtube_page import YoutubePage
from pages.icloud_page import IcloudPage
from pages.tiktok_page import TiktokPage
from applications.bittorent import Bittorrent


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

        # Load configuration data and test site data from JSON files
        with open(config_dir, "r") as json_file:
            self.config_data = json.load(json_file)
        with open(testsites_dir, "r") as test_sites_json_file:
            self.test_sites_data = json.load(test_sites_json_file)

        # Initialize page objects
        self.youtube_page = YoutubePage(self.driver, self.test_sites_data)
        self.telemetry = Telemetry(self.driver, self.config_data)
        self.messenger_page = MessengerPage(self.driver, self.test_sites_data)
        self.soundcloud_page = SoundcloudPage(
            self.driver, self.test_sites_data)
        self.twitter_page = TwitterPage(self.driver, self.test_sites_data)
        self.nexusmods_page = NexusModsPage(self.driver, self.test_sites_data)
        self.microsoft_page = MicrosoftPage(self.driver, self.test_sites_data)
        self.icloud_page = IcloudPage(self.driver, self.test_sites_data)
        self.tiktok_page = TiktokPage(self.driver, self.test_sites_data)
        self.bittorrent = Bittorrent(self.driver, self.test_sites_data)
        self.driver.maximize_window()

    # Needs subscription to upload/download more files
    def test_icloud_download(self):
        # Sign in script requires text code authentication. Must login manually.
        self.icloud_page.run_icloud_download(180)
        self.telemetry.run_telemetry_test('Microsoft', 'DOWNLOAD', True, self.icloud_page.interaction)

    #  Needs subscription to upload/download more files
    def test_icloud_upload(self):
        self.icloud_page.run_icloud_upload(180)
        self.telemetry.run_telemetry_test('iCloud', 'UPLOAD', True, self.icloud_page.interaction)

    def test_messenger_conference(self):
        self.messenger_page.run_messenger_conference(180)
        self.telemetry.run_telemetry_test('Facebook', 'CONFERENCE', True, self.messenger_page.interaction)

    def test_microsoft_download(self):
        self.microsoft_page.run_microsoft_download(180)
        self.telemetry.run_telemetry_test('Microsoft', 'DOWNLOAD', True, self.microsoft_page.interaction)

    def test_nexusmods_download(self):
        self.nexusmods_page.run_nexusmods_download(180)
        self.telemetry.run_telemetry_test('NexusMods', 'DOWNLOAD', True, self.nexusmods_page.interaction)

    def test_soundcloud_music(self):
        self.soundcloud_page.run_soundcloud_music(180)
        self.telemetry.run_telemetry_test('SoundCloud', 'MUSIC', True, self.soundcloud_page.interaction)

    def test_soundcloud_upload(self):
        self.soundcloud_page.run_soundcloud_upload(180)
        self.telemetry.run_telemetry_test('SoundCloud', 'UPLOAD', True, self.soundcloud_page.interaction)

    def test_tiktok_social(self):
        self.tiktok_page.run_tiktok_social(180)
        self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True, self.tiktok_page.interaction)

    def test_twitter_social(self):
        self.twitter_page.run_twitter_social(180)
        self.telemetry.run_telemetry_test('Twitter', 'SOCIAL', True, self.twitter_page.interaction)

    def test_youtube_streaming(self):
        self.youtube_page.run_youtube_streaming(180)
        self.telemetry.run_telemetry_test('Youtube', 'STREAMING', True, self.youtube_page.interaction)

    def test_youtube_download(self):
        self.youtube_page.run_youtube_download(180)
        self.telemetry.run_telemetry_test('Youtube', 'DOWNLOAD', True, self.youtube_page.interaction_download)

    # def test_bittorrent_download(self):
    #
    #     self.bittorrent.run_bittorrent_download()
    #     time.sleep(3000)

    def tearDown(self):
        # Close the browser
        self.driver.quit()
