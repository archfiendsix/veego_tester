import time
from selenium.webdriver.common.by import By
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

    def run_youtube_streaming(self, timeout=180):

        self.driver.maximize_window()

        self.driver.get(self.test_sites['youtube_streaming'])

        time.sleep(2)
        # self.actions.send_keys('k').perform()

        try:
            player_paused = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#movie_player.paused-mode"))
            )
            self.actions.send_keys('0').perform()
            self.actions.send_keys('k').perform()
        except (NoSuchElementException, TimeoutException):
            # Elements not found, so the user is probably already signed in
            pass

        self.logger(f'\nPlaying Youtube video... \n')

        self.timout_while_interact(timeout)
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
        self.logger("\nVideo Already Downloaded. Deleting download...")
        download_button_locator = (
            By.CSS_SELECTOR, 'button[aria-label="Downloaded"]')
        download_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                download_button_locator)
        )
        download_button.click()
        dialog_delete_locator = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
        dialog_delete = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                dialog_delete_locator)
        )
        dialog_delete.click()

    def run_youtube_download(self, timeout=180):


        self.driver.get(self.test_sites["youtube_download"])

        try:
            player_paused = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#movie_player.paused-mode"))
            )

        except (NoSuchElementException, TimeoutException):
            self.actions.send_keys('k').perform()

        try:
            download_button_locator = (
                By.CSS_SELECTOR, 'button[aria-label="Download"]')
            download_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    download_button_locator)
            )

        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            self.delete_video_download()

        download_button.click()
        self.logger(f'\nYoutube Download Started... \n')

        self.timout_while_interact(timeout)
