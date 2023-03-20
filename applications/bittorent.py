
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class Bittorrent(BasePage):


    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_bittorrent_download(self, timeout):
        self.driver.get(
            self.test_sites['bittorrent_download'])
        time.sleep(5)
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('return')
        time.sleep(10)
        self.open_window("BitTorrent")
        self.open_window("Add New Torrent")
        time.sleep(10)
        pyautogui.press('enter')
        pyautogui.press('return')

        self.logger("Bittorrent download started...")
        self.interaction(timeout)
        # WebDriverWait(self.driver, 20).until(EC.alert_is_present())
        # alert = self.driver.switch_to.alert
        # alert.accept()
        # # self.driver.find_element(By.CSS_LOCATOR, "body").send_keys(Keys.TAB)
        # # body_locator = (By.CSS_SELECTOR, "body")
        # # self.wait_and_execute(self.driver,body_locator, 10, lambda elem: (elem.click(), elem.send_keys(Keys.TAB), elem.send_keys(Keys.ENTER)))
        # Create an instance of ActionChains
        # actions = ActionChains(self.driver)

        # Send keys to the active window
        # actions.send_keys(Keys.ENTER).perform()
        # Wait for the "Open BitTorrent" button to appear
        # Locate the "Open BitTorrent" button on the screen
        # png_dir = os.path.abspath(os.path.join(os.getcwd(), "open_bittorrent_button.png"))
        # button_location = pyautogui.locateOnScreen(png_dir)

        # cwd = os.getcwd()
        # print(cwd)
        #
        # file_path = os.path.join(cwd, "open_bittorrent_button.png")
        # print(file_path)
        #
        # print(os.path.exists(file_path))

        # print(os.path.abspath(os.path.join(os.getcwd(), "open_bittorrent_button.png")))
        # image_path = os.path.abspath(os.path.join(os.getcwd(), "open_bittorrent_button.png"))

        # pyautogui.click(os.path.abspath(os.path.join(os.getcwd(), "open_bittorrent_button.png")))
        # Click on the button
        # pyautogui.click(button_location)
