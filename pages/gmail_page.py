import pyautogui as py
from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class GmailPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_gmail_game(self, timeout):
        self.driver.get(
            self.test_sites['gmail_email'])
        time.sleep(5)
        x = py.size()
        height = x.height
        width = x.width
        center_height = x.height // 2
        center_width = x.width // 2
        py.moveTo(center_width - (width * (0.15)), center_height - (height // 4) + (height * (-0.06)), duration=0.25)  #
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        py.moveTo(center_width - (width * (0.08)), center_height - (height // 4) + (height * (-0.06)),duration=0.25)  #
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        py.moveTo(center_width - (width * (0.15)), center_height - (height // 4) + (height * (-0.06)), duration=0.25)  #
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        self.logger("Gmail Email started...")
        self.interaction(timeout)



#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# driver = ucdriver.Chrome()
# time.sleep(1)
# driver.get('https://mail.google.com/mail/u/0/?tab=wm#inbox')
# driver.maximize_window()
# driver.implicitly_wait(300)
# driver.find_element(By.XPATH, '//*[@id="identifierId"]').click()
# driver.implicitly_wait(300)
# driver.find_element(By.XPATH, GOOGLE_MEET_EMAIL_TEXTFIELD).send_keys("autoveego@gmail.com")
# driver.implicitly_wait(300)
# driver.find_element(By.XPATH, GOOGLE_MEET_NEXT_BUTTON).click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('veego2023')
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
# time.sleep(1)
# x = py.size()
# height = x.height
# width = x.width
# center_height = x.height // 2
# center_width = x.width // 2
# time.sleep(2)
# py.moveTo(center_width - (width * (0.33)), center_height - (height // 4) + (height * (0.10)), duration=0.25  )  # arrive to password
# time.sleep(2)
# pyautogui.click()
# py.moveTo(center_width - (width * ( 0.9)), center_height - (height // 4) + (height * ( 0.66)), duration=0.25  )  # scroll on linkdin
# time.sleep(2)
# pyautogui.click()
# time.sleep(3)