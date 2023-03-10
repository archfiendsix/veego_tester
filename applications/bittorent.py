
import os
import pyautogui

from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class Bittorrent(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10


    def run_bittorrent_download(self):
        self.driver.get(
            "magnet:?xt=urn:btih:F2E6914B4C30B7F6EF9A621E7C5133B8839CBD11&dn=Cyberpunk+2077+v6.15+%282021+Update%29&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2F47.ip-51-68-199.eu%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce")
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

        cwd = os.getcwd()
        print(cwd)

        file_path = os.path.join(cwd, "open_bittorrent_button.png")
        print(file_path)

        print(os.path.exists(file_path))

        # print(os.path.abspath(os.path.join(os.getcwd(), "open_bittorrent_button.png")))
        # image_path = os.path.abspath(os.path.join(os.getcwd(), "open_bittorrent_button.png"))
        image_coords = pyautogui.locateOnScreen(file_path)
        if image_coords is not None:
            pyautogui.click(image_coords)
        else:
            print(f"Image not found on screen: {file_path}")
        # pyautogui.click(os.path.abspath(os.path.join(os.getcwd(), "open_bittorrent_button.png")))
        # Click on the button
        # pyautogui.click(button_location)