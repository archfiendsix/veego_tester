import json
import os
import unittest

from pages.espn_page import EspnPage
from pages.facebook_page import FacebookPage
from pages.twitch_page import TwitchPage
from pages.zoom_page import ZoomPage
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
from applications.ms_store import MSStore
from pages.googleMeet_page import GoogleMeetPage
from pages.teams_page import TeamsPage
from pages.roblox_page import RobloxPage
from pages.gmail_page import GmailPage
from pages.amazonPrime_page import AmazonPrimePage
from pages.linkedin_page import LinkedinPage
from pages.instagram_page import InstagramPage
from pages.netflix_page import NetflixPage
from pages.dropbox_page import DropboxPage
from pages.spotify_page import SpotifyPage
from pages.pcloud_page import PcloudPage
from pages.speed_page import SpeedPage

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
        self.soundcloud_page = SoundcloudPage(self.driver, self.test_sites_data)
        self.twitter_page = TwitterPage(self.driver, self.test_sites_data)
        self.nexusmods_page = NexusModsPage(self.driver, self.test_sites_data)
        self.microsoft_page = MicrosoftPage(self.driver, self.test_sites_data)
        self.icloud_page = IcloudPage(self.driver, self.test_sites_data)
        self.tiktok_page = TiktokPage(self.driver, self.test_sites_data)
        self.bittorrent = Bittorrent(self.driver, self.test_sites_data)
        self.msstore = MSStore(self.driver, self.test_sites_data)
        self.twitch_page = TwitchPage(self.driver, self.test_sites_data)
        self.espn_page = EspnPage(self.driver, self.test_sites_data)
        self.facebook_page = FacebookPage(self.driver, self.test_sites_data)
        self.zoom_page = ZoomPage(self.driver, self.test_sites_data)
        self.googleMeet_page = GoogleMeetPage(self.driver, self.test_sites_data)
        self.teams_page = TeamsPage(self.driver, self.test_sites_data)
        self.roblox_page = RobloxPage(self.driver, self.test_sites_data)
        self.gmail_page = GmailPage(self.driver, self.test_sites_data)
        self.amazonPrime_page = AmazonPrimePage(self.driver, self.test_sites_data)
        self.linkedin_page = LinkedinPage(self.driver, self.test_sites_data)
        self.netflix_page = NetflixPage(self.driver, self.test_sites_data)
        self.instagram_page = InstagramPage(self.driver, self.test_sites_data)
        self.dropbox_page = DropboxPage(self.driver, self.test_sites_data)
        self.spotify_page = SpotifyPage(self.driver, self.test_sites_data)
        self.pcloud_page = PcloudPage(self.driver, self.test_sites_data)
        self.speed_page = SpeedPage(self.driver, self.test_sites_data)

        self.driver.maximize_window()

    # Needs subscription to upload/download more files
    def test_icloud_download(self):
        # Sign in script requires text code authentication. Must log in manually.
        self.icloud_page.run_icloud_download(100)
        self.telemetry.run_telemetry_test('iCloud', 'DOWNLOAD', True, self.icloud_page.interaction)

    #  Needs subscription to upload/download more files
    # def test_icloud_upload(self):
    #     self.icloud_page.run_icloud_upload(120)
    #     self.telemetry.run_telemetry_test('iCloud', 'UPLOAD', True, self.icloud_page.interaction)

    def test_pcloud_upload(self):
        self.pcloud_page.run_pcloud_upload(180)
        self.telemetry.run_telemetry_test('pcloud', 'UPLOAD', True, self.pcloud_page.interaction)

    def test_dropbox_download(self):
        self.dropbox_page.run_dropbox_download(180)
        self.telemetry.run_telemetry_test('Dropbox', 'DOWNLOAD', True, self.dropbox_page.interaction)

    # def test_dropbox_upload(self):
    #     self.dropbox_page.run_dropbox_upload(180)
    #     self.telemetry.run_telemetry_test('Dropbox', 'UPLOAD', True, self.dropbox_page.interaction)
    def test_messenger_conference(self):
        self.messenger_page.run_messenger_conference(180)
        self.telemetry.run_telemetry_test('Facebook', 'SOCIAL', True, self.messenger_page.interaction)

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
        # Need Premium account
        self.soundcloud_page.run_soundcloud_upload(180)
        self.telemetry.run_telemetry_test('SoundCloud', 'UPLOAD', True, self.soundcloud_page.interaction)

    def test_soundcloud_download(self):
        # Need Premium account
        self.soundcloud_page.run_soundcloud_download(180)
        self.telemetry.run_telemetry_test('SoundCloud', 'DOWNLOAD', True, self.soundcloud_page.interaction)

    def test_tiktok_social(self):
        self.tiktok_page.run_tiktok_social(80)
        self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True, self.tiktok_page.interaction)

    def test_twitter_social(self):
        self.twitter_page.run_twitter_social(180)
        self.telemetry.run_telemetry_test('Twitter', 'SOCIAL', True, self.twitter_page.interaction)

    def test_youtube_streaming(self):
        self.youtube_page.run_youtube_streaming(30)
        self.telemetry.run_telemetry_test('Youtube', 'STREAMING', True, self.youtube_page.interaction)
    def test_spotify_music(self):
        self.spotify_page.run_spotify_music(180)
        self.telemetry.run_telemetry_test('Spotify', 'MUSIC', True, self.spotify_page.interaction)

    def test_zoom_conference(self):
        self.zoom_page.run_zoom_conference(180)
        self.telemetry.run_telemetry_test('Zoom', 'CONFERENCING', True, self.zoom_page.interaction)

    def test_teams_conference(self):
        self.teams_page.run_teams_conference(180)
        self.telemetry.run_telemetry_test('MSTeams/Skype', 'CONFERENCING', True, self.zoom_page.interaction)
    def test_GoogleMeet_conference(self):
        self.googleMeet_page.run_googleMeet_conference(180)
        self.telemetry.run_telemetry_test('GoogleMeet', 'CONFERENCING', True, self.googleMeet_page.interaction)

    def test_roblox_game(self):
        self.roblox_page.run_roblox_game(180)
        self.telemetry.run_telemetry_test('Roblox', 'GAMING', True, self.roblox_page.interaction)

    def test_gmail_mail(self):
        self.gmail_page.run_gmail_mail(80)
        self.telemetry.run_telemetry_test('Gmail', 'MAIL', True, self.gmail_page.interaction)
    def test_amazonPrime_game(self):
        self.amazonPrime_page.run_amazonPrime_streaming(180)
        self.telemetry.run_telemetry_test('AmazonPrime', 'STREAMING', True, self.amazonPrime_page.interaction)

    def test_linkedin_social(self):
        self.linkedin_page.run_linkedin_social(80)
        self.telemetry.run_telemetry_test('Linkedin', 'SOCIAL', True, self.linkedin_page.interaction)

    def test_instagram_social(self):
        self.instagram_page.run_instagram_social(80)
        self.telemetry.run_telemetry_test('Instagram', 'SOCIAL', True, self.instagram_page.interaction)

    def test_facebook_social(self):
        self.facebook_page.run_facebook_social(80)
        self.telemetry.run_telemetry_test('Facebook', 'SOCIAL', True, self.facebook_page.interaction)
    def test_netflix_streaming(self):
        self.netflix_page.run_netflix_streaming(180)
        self.telemetry.run_telemetry_test('Netflix', 'STREAMING', True, self.netflix_page.interaction)

    def test_espn_streaming(self):
        self.espn_page.run_espn_streaming(180)
        self.telemetry.run_telemetry_test('ESPN', 'STREAMING', True, self.espn_page.interaction)

    def test_twitch_streaming(self):
        self.twitch_page.run_twitch_streaming(180)
        self.telemetry.run_telemetry_test('Twitch', 'STREAMING', True, self.twitch_page.interaction)
    def test_speed_download(self):
        self.speed_page.run_speed_download(100)
        self.telemetry.run_telemetry_test('Speed', 'DOWNLOAD', True, self.speed_page.interaction)

    def test_youtube_download(self):
        self.youtube_page.run_youtube_download(180)
        self.telemetry.run_telemetry_test('Youtube', 'DOWNLOAD', True, self.youtube_page.interaction_download)

    # Not Yet Working
    def test_bittorrent_download(self):

        self.bittorrent.run_bittorrent_download(180)
        self.telemetry.run_telemetry_test('Torrent', 'TORRENT', True, self.youtube_page.interaction_download)

    def test_msstore_download(self):

        self.msstore.run_msstore_download(180)
        self.telemetry.run_telemetry_test('Microsoft', 'DOWNLOAD', True, self.youtube_page.interaction_download)

    def tearDown(self):
        # Close the browser
        self.driver.quit()
