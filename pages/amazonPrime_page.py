
from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class AmazonPrimePage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_amazonPrime_streaming(self, timeout):
        self.driver.get(
            self.test_sites['amazonPrime_streaming'])
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="dv-action-box"]/div/div/div/div[2]/div/div/div/a').click()
        time.sleep(1)
        self.logger("AmazonPrime streaming started...")
        self.interaction(timeout)



#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# driver = ucdriver.Chrome()
# time.sleep(1)
# driver.get('https://www.primevideo.com/region/eu/?ref_=atv_auth_pre')
# # driver.get('https://apps.google.com/meet/')
# driver.maximize_window()
# driver.implicitly_wait(300)
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="pv-nav-sign-in"]').send_keys(Keys.ENTER)
# driver.implicitly_wait(300)
# time.sleep(2)
# action1 = ActionChains(driver)
# action1.send_keys("daniel@veego.io")
# action1.perform()
# driver.implicitly_wait(300)
# # TAB
# action2 = ActionChains(driver)
# action2.send_keys(Keys.TAB)
# action2.perform()
# driver.implicitly_wait(300)
# # Password
# action3 = ActionChains(driver)
# action3.send_keys("Trigger1984")
# action3.perform()
# driver.implicitly_wait(300)
# time.sleep(1)
# # connect
# action4 = ActionChains(driver)
# action4.send_keys(Keys.ENTER)
# action4.perform()
# driver.implicitly_wait(300)
# time.sleep(3)
#
# x = py.size()
# height = x.height
# width = x.width
# center_height = x.height // 2
# center_width = x.width // 2
# py.moveTo(center_width - (width * (0.2990)), center_height - (height // 4) + (height * (0.2)), duration=0.25)
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# py.click()
# action4 = ActionChains(driver)
# action4.send_keys(Keys.ENTER)
# action4.perform()
# time.sleep(2)
# pyautogui.click()
#
# py.moveTo(center_width - (width * (-0.1)), center_height - (height // 4) + (height * (0.29)), duration=0.25)
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# # py.click()
# # action4 = ActionChains(driver)
# # action4.send_keys(Keys.ENTER)
# # action4.perform()
# time.sleep(2)
# pyautogui.click()
# time.sleep(10)