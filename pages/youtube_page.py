import time
from selenium import webdriver
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
        self.actions.send_keys('k').perform()
        self.logger(f'\nPlaying Youtube video... \n')

        time.sleep(timeout)
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
        downloadedButton_locator = (
            By.CSS_SELECTOR, 'button[aria-label="Downloaded"]')
        downloadedButton = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                downloadedButton_locator)
        )
        downloadedButton.click()
        dialogDelete_locator = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
        dialogDelete = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                dialogDelete_locator)
        )
        dialogDelete.click()

    def run_youtube_download(self, timeout=180):

        self.driver.maximize_window()

        self.driver.get(self.test_sites["youtube_download"])

        try:
            self.actions.send_keys('k').perform()
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

        time.sleep(timeout)
