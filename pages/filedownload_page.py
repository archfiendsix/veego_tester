from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class FiledownloadPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_filedownload_download(self, timeout):
        self.driver.get( self.test_sites['filedownload_download'])
        time.sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="main"]/article/div/div[1]/div[1]/div[1]/a').click()
        time.sleep(10)
        self.logger("Filedownload download started...")
        self.interaction(timeout)