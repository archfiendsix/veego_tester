import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from pages.base_page import BasePage


class YoutubePage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites

    def interaction(self, timeout):
        body_locator = (By.CSS_SELECTOR, 'body')
        self.wait_and_execute(self.driver, body_locator, 5, lambda elem: elem.send_keys("0"))
        time.sleep(timeout)
    def interaction_download(self, timeout):
        start_time = time.time()
        download_button_locator = (By.CSS_SELECTOR, 'button[aria-label="Download"]')
        downloaded_button_locator = (By.CSS_SELECTOR, 'button[aria-label="Downloaded"]')
        downloading_button_locator = (By.CSS_SELECTOR, 'button[aria-label="Downloading"]')
        while time.time() - start_time < timeout:
            try:
                self.wait_and_execute(self.driver, download_button_locator, 3, lambda elem: elem.click())
            except (NoSuchElementException, TimeoutException):
                try:
                    self.wait_and_execute(self.driver, downloaded_button_locator, 3, lambda elem: elem.click())
                    delete_all_delete_locator = (By.CSS_SELECTOR, 'tp-yt-paper-dialog button[aria-label="Delete"]')
                    self.wait_and_execute(self.driver, delete_all_delete_locator, 3, lambda elem: elem.click())
                except (NoSuchElementException, TimeoutException):
                    continue
    def run_youtube_streaming(self, timeout=180):


        self.driver.get(self.test_sites['youtube_streaming'])

        try:
            player_paused = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#movie_player.paused-mode"))
            )

            self.actions.send_keys('k').perform()
        except (NoSuchElementException, TimeoutException):
            # Elements not found, so the user is probably already signed in
            pass

        self.logger(f'\nPlaying Youtube video... \n')

        self.interaction(timeout)
        # 180

    def download_video(self):

        download_button_locator = (
            By.CSS_SELECTOR, 'button[aria-label="Download"]')
        download_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                download_button_locator)
        )
        download_button.click()
        self.logger(f'\nStarting Youtube Download... \n')

    def delete_video_download(self):
        self.driver.get("https://www.youtube.com/account_downloads")
        delete_all_downloads_locator = (By.CSS_SELECTOR, 'button[aria-label="Delete all downloads"]')
        self.wait_and_execute(self.driver, delete_all_downloads_locator, 5, lambda elem: elem.click())
        delete_all_delete_locator = (By.CSS_SELECTOR, 'tp-yt-paper-dialog button[aria-label="Delete"]')
        self.wait_and_execute(self.driver, delete_all_delete_locator, 5, lambda elem: elem.click())
        time.sleep(5)



    def run_youtube_download(self, timeout=180):


        try:
            self.delete_video_download()
        except (NoSuchElementException, TimeoutException):
            pass




        start_time = time.time()

        self.driver.get(self.test_sites["youtube_download"])

        # try:
        #     player_paused = WebDriverWait(self.driver, 6).until(
        #         EC.presence_of_element_located(
        #             (By.CSS_SELECTOR, "#movie_player.paused-mode"))
        #     )
        #
        # except (NoSuchElementException, TimeoutException):
        #     self.actions.send_keys('k').perform()


        self.interaction(timeout)
