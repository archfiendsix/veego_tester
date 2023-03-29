
import time
import pyautogui as py
import pyautogui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver import Keys, ActionChains
from pages.base_page import BasePage

class EspnPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        # self.timeout = 10

    def interaction(self, timeout):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.actions.send_keys('1').perform()
        time.sleep(timeout)

    def run_espn_streaming(self, timeout=180):

        self.driver.get(self.test_sites['espn_streaming'])
        self.driver.maximize_window()
        time.sleep(1)
        try:
            close_cookie_locator = (
            By.CSS_SELECTOR, ".onetrust-close-btn-handler.onetrust-close-btn-ui.banner-close-button.ot-close-icon")
            self.wait_and_execute(self.driver, close_cookie_locator, 10, lambda elem: elem.click())
        except (NoSuchElementException, TimeoutException, NoAlertPresentException):
            pass
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        time.sleep(3)
        py.moveTo(center_width - (width * (-0.9)), center_height - (height // 4) + (height * (0.3)), duration=0.25)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        py.moveTo(center_width - (width * (-0.9)), center_height - (height // 4) + (height * (0.3)), duration=0.25)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        py.moveTo(center_width - (width * (0.1)), center_height - (height // 4) + (height * (0.3)), duration=0.25)
        pyautogui.click()


        # self.actions.send_keys('k').perform()
        self.logger(f'\nRunning Espn Streaming... \n')

        self.interaction(timeout)
        # 180
