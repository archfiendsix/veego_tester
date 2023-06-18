
import time
import pyautogui as py
import pyautogui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver import Keys, ActionChains
from pages.base_page import BasePage

class HboPage(BasePage):
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

    def run_hbo_streaming(self, timeout=30):

        self.driver.get(self.test_sites['hbo_streaming'])
        self.driver.maximize_window()
        time.sleep(1)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="page17387-band61935-Button232922"]').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(300)
        time.sleep(2)
        pyautogui.click()
        time.sleep(5)
        py.moveTo(center_width - (width * (0.17)), center_height - (height // 4) + (height * (0.4)), duration=0.25)
        time.sleep(3)
        pyautogui.click()
        pyautogui.click()
        # time.sleep(50)
        # py.moveTo(center_width - (width * (0.19)), center_height - (height // 4) + (height * (0.52)),duration=0.25)
        # pyautogui.click()
        # pyautogui.click()
        # self.actions.send_keys('k').perform()
        self.logger(f'\nRunning Hbo Streaming... \n')

        self.interaction(timeout)
        # 180
