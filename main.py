import json
import os
import unittest
# from venv import logger
from pages.webex_page import WebexPage
from pages.espn_page import EspnPage
from pages.facebook_page import FacebookPage
from pages.squidtv_page import SquidtvPage
from pages.twitch_page import TwitchPage
from pages.zoom_page import ZoomPage
from pages.skype_page import SkypePage
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
from pages.googledrive_page import GoogledrivePage
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
from pages.squidtv_page import SquidtvPage
from pages.hbo_page import HboPage
from pages.filedownload_page import FiledownloadPage

# @pytest.mark.sanity
# class kill_process():
#     # logger('clean_computer')
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
#     # logger.info('ending clean_computer')
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
        self.googledrive_page = GoogledrivePage(self.driver, self.test_sites_data)
        self.teams_page = TeamsPage(self.driver, self.test_sites_data)
        self.skype_page = SkypePage(self.driver, self.test_sites_data)
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
        self.squidtv_page = SquidtvPage(self.driver, self.test_sites_data)
        self.filedownload_page = FiledownloadPage(self.driver, self.test_sites_data)
        self.hbo_page = HboPage(self.driver, self.test_sites_data)

        self.webex_page = WebexPage(self.driver, self.test_sites_data)
        self.resource = self._get_resource_info(self.config_data, "windows")
        self.driver.maximize_window()

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



    ''' Needs subscription to upload/download more files'''
    # def test_icloud_download(self):
    #     # Sign in script requires text code authentication. Must log in manually.
    #     self.icloud_page.run_icloud_download(100)
    #     self.telemetry.run_telemetry_test('iCloud', 'DOWNLOAD', True, self.icloud_page.interaction)

    #  Needs subscription to upload/download more files
    # def test_icloud_upload(self):
    #     self.icloud_page.run_icloud_upload(120)
    #     self.telemetry.run_telemetry_test('iCloud', 'UPLOAD', True, self.icloud_page.interaction)

    def test_pcloud_upload(self):
        # kill_process()
        self.pcloud_page.run_pcloud_upload(130)
        self.telemetry.run_telemetry_test('pcloud', 'UPLOAD', True, self.pcloud_page.interaction,mac=self.resource['mac'])

    def test_pcloud_download(self):
        # kill_process()
        self.pcloud_page.run_pcloud_download(130)
        self.telemetry.run_telemetry_test('pcloud', 'DWONLOAD', True, self.pcloud_page.interaction,mac=self.resource['mac'])

    def test_googledrive_upload(self):
        kill_process()
        self.googledrive_page.run_googledrive_upload(130)
        self.telemetry.run_telemetry_test('Google_DRIVE', 'UPLOAD', True, self.pcloud_page.interaction,
                                          mac=self.resource['mac'])

    def test_googledrive_download(self):
        kill_process()
        self.googledrive_page.run_googledrive_download(130)
        self.telemetry.run_telemetry_test('GOOGO_DRIVE', 'DOWNLOAD', True, self.pcloud_page.interaction,
                                          mac=self.resource['mac'])
    def test_dropbox_download(self):
        kill_process()
        self.dropbox_page.run_dropbox_download(130)
        self.telemetry.run_telemetry_test('Dropbox', 'DOWNLOAD', True, self.dropbox_page.interaction,mac=self.resource['mac'])

    '''Needs subscription to upload files'''
    # def test_dropbox_upload(self):
    #     self.dropbox_page.run_dropbox_upload(180)
    #     self.telemetry.run_telemetry_test('Dropbox', 'UPLOAD', True, self.dropbox_page.interaction,mac=self.resource['mac'])

    # def test_messenger_conference(self):
    #     self.messenger_page.run_messenger_conference(180)
    #     self.telemetry.run_telemetry_test('Facebook', 'SOCIAL', True, self.messenger_page.interaction,mac=self.resource['mac'])

    def test_microsoft_download(self):
        kill_process()
        self.microsoft_page.run_microsoft_download(130)
        self.telemetry.run_telemetry_test('Microsoft', 'DOWNLOAD', True, self.microsoft_page.interaction,mac=self.resource['mac'])

    '''Needs subscription to download files'''
    # def test_nexusmods_download(self):
    #     self.nexusmods_page.run_nexusmods_download(180)
    #     self.telemetry.run_telemetry_test('NexusMods', 'DOWNLOAD', True, self.nexusmods_page.interaction,mac=self.resource['mac'])

    def test_soundcloud_music(self):
        kill_process()
        self.soundcloud_page.run_soundcloud_music(120)
        self.telemetry.run_telemetry_test('SoundCloud', 'MUSIC', True, self.soundcloud_page.interaction, mac=self.resource['mac'])

    '''Needs subscription to upload files'''
    # def test_soundcloud_upload(self):
    #     # Need Premium account
    #     self.soundcloud_page.run_soundcloud_upload(180)
    #     self.telemetry.run_telemetry_test('SoundCloud', 'UPLOAD', True, self.soundcloud_page.interaction, mac=self.resource['mac'])

    # def test_soundcloud_download(self):
    #     # Need Premium account
    #     self.soundcloud_page.run_soundcloud_download(180)
    #     self.telemetry.run_telemetry_test('SoundCloud', 'DOWNLOAD', True, self.soundcloud_page.interaction, mac=self.resource['mac'])

    def test_tiktok_social(self):
        kill_process()
        self.tiktok_page.run_tiktok_social(80)
        self.telemetry.run_telemetry_test('Tiktok', 'SOCIAL', True, self.tiktok_page.interaction,mac=self.resource['mac'])

    def test_twitter_social(self):
        kill_process()
        self.twitter_page.run_twitter_social(80)
        self.telemetry.run_telemetry_test('Twitter', 'SOCIAL', True, self.twitter_page.interaction,mac=self.resource['mac'])

    def test_youtube_streaming(self):
        kill_process()
        self.youtube_page.run_youtube_streaming(130)
        self.telemetry.run_telemetry_test('Youtube', 'STREAMING', True, self.youtube_page.interaction,mac=self.resource['mac'])
    def test_spotify_music(self):
        kill_process()
        self.spotify_page.run_spotify_music(100)
        self.telemetry.run_telemetry_test('Spotify', 'MUSIC', True, self.spotify_page.interaction,mac=self.resource['mac'])

    def test_zoom_conference(self):
        kill_process()
        self.zoom_page.run_zoom_conference(130)
        self.telemetry.run_telemetry_test('Zoom', 'CONFERENCING', True, self.zoom_page.interaction,mac=self.resource['mac'])
    def test_skype_conference(self):
        kill_process()
        self.skype_page.run_skype_conference(80)
        self.telemetry.run_telemetry_test('MSTeams/Skype', 'CONFERENCING', True, self.skype_page.interaction,mac=self.resource['mac'])

    def test_webex_conference(self):
        kill_process()
        self.webex_page.run_webex_conference(80)
        self.telemetry.run_telemetry_test('webex', 'CONFERENCING', True, self.skype_page.interaction, mac=self.resource['mac'])

    def test_teams_conference(self):
        kill_process()
        self.teams_page.run_teams_conference(80)
        self.telemetry.run_telemetry_test('MSTeams/Skype', 'CONFERENCING', True, self.teams_page.interaction,mac=self.resource['mac'])

    def test_googleMeet_conference(self):
        kill_process()
        self.googleMeet_page.run_googleMeet_conference(130)
        self.telemetry.run_telemetry_test('GoogleMeet', 'CONFERENCING', True, self.googleMeet_page.interaction,mac=self.resource['mac'])

    def test_roblox_game(self):
        kill_process()
        self.roblox_page.run_roblox_game(120)
        self.telemetry.run_telemetry_test('Roblox', 'GAMING', True, self.roblox_page.interaction,mac=self.resource['mac'])

    def test_gmail_mail(self):
        kill_process()
        self.gmail_page.run_gmail_mail(80)
        self.telemetry.run_telemetry_test('Gmail', 'MAIL', True, self.gmail_page.interaction,mac=self.resource['mac'])

    def test_amazonPrime_streaming(self):
        kill_process()
        self.amazonPrime_page.run_amazonPrime_streaming(120)
        self.telemetry.run_telemetry_test('AmazonPrime', 'STREAMING', True, self.amazonPrime_page.interaction,mac=self.resource['mac'])

    def test_linkedin_social(self):
        kill_process()
        self.linkedin_page.run_linkedin_social(80)
        self.telemetry.run_telemetry_test('Linkedin', 'SOCIAL', True, self.linkedin_page.interaction,mac=self.resource['mac'])

    def test_instagram_social(self):
        kill_process()
        self.instagram_page.run_instagram_social(80)
        self.telemetry.run_telemetry_test('Instagram', 'SOCIAL', True, self.instagram_page.interaction,mac=self.resource['mac'])

    def test_facebook_social(self):
        kill_process()
        self.facebook_page.run_facebook_social(80)
        self.telemetry.run_telemetry_test('Facebook', 'SOCIAL', True, self.facebook_page.interaction,mac=self.resource['mac'])

    def test_netflix_streaming(self):
        kill_process()
        self.netflix_page.run_netflix_streaming(130)
        self.telemetry.run_telemetry_test('Netflix', 'STREAMING', True, self.netflix_page.interaction,mac=self.resource['mac'])

    def test_squidtv_streaming(self):
        kill_process()
        self.squidtv_page.run_squidtv_streaming(130)
        self.telemetry.run_telemetry_test('Squidtv', 'STREAMING', True, self.squidtv_page.interaction, mac=self.resource['mac'])

    def test_espn_streaming(self):
        kill_process()
        self.espn_page.run_espn_streaming(120)
        self.telemetry.run_telemetry_test('ESPN', 'STREAMING', True, self.espn_page.interaction,mac=self.resource['mac'])

    def test_hbo_streaming(self):
        kill_process()
        self.hbo_page.run_hbo_streaming(20)
        self.telemetry.run_telemetry_test('HBO', 'STREAMING', True, self.hbo_page.interaction,mac=self.resource['mac'])

    def test_twitch_streaming(self):
        kill_process()
        self.twitch_page.run_twitch_streaming(130)
        self.telemetry.run_telemetry_test('Twitch', 'STREAMING', True, self.twitch_page.interaction,mac=self.resource['mac'])
    def test_speed_download(self):
        kill_process()
        self.speed_page.run_speed_download(120)
        self.telemetry.run_telemetry_test('Speed', 'DOWNLOAD', True, self.speed_page.interaction,mac=self.resource['mac'])

    def test_filedownload_download(self):
        kill_process()
        self.filedownload_page.run_filedownload_download(120)
        self.telemetry.run_telemetry_test('Filedownload', 'DOWNLOAD', True, self.speed_page.interaction,mac=self.resource['mac'])

    def test_youtube_download(self):
        kill_process()
        self.youtube_page.run_youtube_download(130)
        self.telemetry.run_telemetry_test('Youtube', 'DOWNLOAD', True, self.youtube_page.interaction_download,mac=self.resource['mac'])

    # Not Yet Working
    def test_bittorrent_download(self):
        kill_process()
        self.bittorrent.run_bittorrent_download(50)
        self.telemetry.run_telemetry_test('Torrent', 'TORRENT', True, self.bittorrent.interaction,mac=self.resource['mac'])

    def test_msstore_download(self):
        kill_process()
        self.msstore.run_msstore_download(110)
        self.telemetry.run_telemetry_test('Microsoft', 'DOWNLOAD', True, self.msstore.interaction,mac=self.resource['mac'])

    def tearDown(self):
        # Close the browser
        self.driver.quit()
