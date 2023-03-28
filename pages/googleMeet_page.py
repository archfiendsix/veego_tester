from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class GoogleMeetPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_googleMeet_conference(self, timeout):
        self.driver.get(
            self.test_sites['googleMeet_conference'])
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div[1]/div[1]/button/span').click()
        time.sleep(1)
        self.logger("GoogleMeet conferencing started...")
        self.interaction(timeout)



# import time
# from pathlib import Path
# from turtle import update
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import undetected_chromedriver as ucdriver
# import pyautogui as py
#
#
# import pyautogui
#
# driver = ucdriver.Chrome()
#
# driver.get('https://meet.google.com/?hs=197')
# time.sleep(1)
#
#
# x = py.size()
# height = x.height
# width = x.width
# center_height = x.height // 2
# center_width = x.width // 2
# time.sleep(2)
# py.moveTo(center_width - (width * (0.35)), center_height - (height // 4) + (height * (0.07)),  duration=0.25)  # arrive to sync
# # driver.implicitly_wait(300)
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
#
#
# driver.find_element(By.XPATH, '//*[@id="drawer"]/div/div[3]/div[1]/div/span[3]/a/button/span').click()
#
# driver.implicitly_wait(300)  # sign In
#
# # driver.implicitly_wait(300)
# time.sleep(1)  # userName
# action1 = ActionChains(driver)
# action1.send_keys("veego.tester@gmail.com")
# action1.perform()
# driver.implicitly_wait(300)
# # TAB
# driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
#
# # action2 = ActionChains(driver)
# # action2.send_keys(Keys.TAB)
# # action2.perform()
# time.sleep(1)
# driver.implicitly_wait(300)  # Password
# action3 = ActionChains(driver)
# action3.send_keys("Qazwsx123!@#")
# action3.perform()
# driver.implicitly_wait(400)
# time.sleep(3)  # Push on "Sign In"
# driver.find_element(By.XPATH, '//*[@id="js_btn_login"]/span').click()
# driver.implicitly_wait(300)
# time.sleep(1)#crashing!!
# # TWITTER_EMAIL =veego.tester@gmail.com
# # TWITTER_PASSWORD =Qazwsx123!@#
#
#
# py.moveTo(center_width - (width * (- 0.12)), center_height - (height // 4) + (height * (0.65)), duration=0.25)  # push on  password saved
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# py.moveTo(center_width - (width * (0.48)), center_height - (height // 4) + (height * (-0.14)), duration=0.25)
# time.sleep(2)
# pyautogui.click()
# time.sleep(120)
