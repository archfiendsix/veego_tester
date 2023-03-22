# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from pages.base_page import BasePage
#
#
# class FacebookPage(BasePage):
#     def __init__(self, driver, test_sites):
#         super().__init__(driver)
#         self.driver = driver
#         self.actions = ActionChains(self.driver)
#         self.test_sites = test_sites
#
#     def facebook_signin(self):
#         self.driver.switch_to.default_content()
#
#         # self.wait_and_execute(
#         #     self.driver, (By.CSS_SELECTOR, 'a[data-testid="loginButton"]'), 10, lambda elem: elem.click())
#         # time.sleep(3000)
#         self.wait_and_execute(
#             self.driver, (By.CSS_SELECTOR, 'input[autocomplete="username"]'), 5,
#             lambda elem: elem.send_keys(self.env_twitter_email))
#
#         self.wait_and_execute(
#             self.driver, (By.XPATH, "//span[contains(text(), 'Next')]"), 5,
#             lambda elem: elem.click())
#
#         self.wait_and_execute(
#             self.driver, (By.CSS_SELECTOR, 'input[type="password"]'), 5,
#             lambda elem: elem.send_keys(self.env_twitter_password))
#
#         self.wait_and_execute(
#             self.driver, (By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]'), 5, lambda elem: elem.click())
#
#     def interaction(self, timeout=180):
#         self.driver.switch_to.window(self.driver.window_handles[0])
#         self.random_scroll(timeout)
#
#     def run_facebook_social(self, timeout=180):
#
#         self.driver.get(self.test_sites["facebook_social"])
#
#         # time.sleep(3000)
#         # try:
#         #     sign_in_to_google_iframe_locator = (
#         #         By.CSS_SELECTOR, 'iframe[title="Sign in with Google Dialog"]')
#         #     iframe = WebDriverWait(self.driver, 20).until(
#         #         EC.presence_of_element_located(
#         #             sign_in_to_google_iframe_locator)
#         #     )
#         #     self.driver.switch_to.frame(iframe)
#         #
#         #     sign_in_to_google_button = (
#         #         By.XPATH, "//div[contains(text(), 'Sign in as Veego')]")
#         #
#         #     self.wait_and_execute(
#         #         self.driver, sign_in_to_google_button, 10, lambda elem: elem.click())
#         #     pass
#         #
#         # except (NoSuchElementException, TimeoutException):
#         #
#         # try:
#         #     self.twitter_signin()
#         # except (NoSuchElementException, TimeoutException):
#         #     self.logger("Twitter Already Logged in")
#         try:
#             signin_iframe_locator = (By.CSS_SELECTOR, 'iframe[title="Sign in with Google Dialog"]')
#             signin_iframe = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located(
#                     signin_iframe_locator)
#             )
#
#             self.driver.switch_to.frame(signin_iframe)
#
#             continue_as = (By.CSS_SELECTOR, '#continue-as')
#
#             self.wait_and_execute(self.driver, continue_as, 5, lambda elem: elem.click())
#         except(NoSuchElementException, TimeoutException):
#             pass
#
#         # self.twitter_signin(self.env_twitter_email, self.env_twitter_password)
#         self.logger(f'\nRunning Facebook Social... \n')
#         self.interaction(timeout)
#
#
#
#
#
#
#
#  import logging
# # import os
# # import pathlib
# # import time
# # from pathlib import Path
# # from turtle import update
# # from selenium.webdriver.common.action_chains import ActionChains
# # from selenium.webdriver.common.keys import Keys
# # import undetected_chromedriver as ucdriver
# # import pyautogui as py
# # # import spotipy
# # # from spotipy.oauth2 import SpotifyClientCredentials
# # import pyautogui
# # import pytest
# # from selenium.webdriver.support.ui import WebDriverWait
# # import selenium
# # from selenium.common.exceptions import NoSuchElementException
# #
# # from selenium.webdriver.chrome.options import Options
# #
# # import urllib3
# # from selenium import webdriver
# # #from webdriver_auto_update import check_driver
# #
# # from selenium.webdriver import Keys, ActionChains
# # from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager
# #
# # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# # driver = ucdriver.Chrome()
# # time.sleep(1)
# # # driver.get('https://www.facebook.com/')
# # # time.sleep(1)
# # driver.get('https://www.messenger.com/')
# # driver.maximize_window()
# # time.sleep(3)
# # driver.find_element(By.XPATH, '//*[@id="email"]').click()
# # driver.maximize_window()
# # action1 = ActionChains(driver)
# # action1.send_keys("veegoveego2019@gmail.com")
# # action1.perform()
# # driver.implicitly_wait(300)
# # # TAB
# # action2 = ActionChains(driver)
# # action2.send_keys(Keys.TAB)
# # action2.perform()
# # driver.implicitly_wait(300)
# # # Password
# # action3 = ActionChains(driver)
# # action3.send_keys("veego2019")
# # action3.perform()
# # driver.implicitly_wait(300)
# # time.sleep(1)
# # # connect
# # action4 = ActionChains(driver)
# # action4.send_keys(Keys.ENTER)
# # action4.perform()
# # driver.implicitly_wait(300)
# #
# # x = py.size()
# # height = x.height
# # width = x.width
# # center_height = x.height // 2
# # center_width = x.width // 2
# # py.moveTo(center_width - (width * ( 0.01)), center_height - (height // 4) + (height * ( 0.45)), duration=0.25)
# # time.sleep(2)
# # pyautogui.click()
# # time.sleep(2)
# # # py.moveTo(center_width - (width * (- 0.2990)), center_height - (height // 4) + (height * (- 0.02)), duration=0.25)
# # time.sleep(2)
# # pyautogui.click()
# # time.sleep(2)
# # # py.moveTo(center_width - (width * (0.33)), center_height - (height // 4) + (height * (0.10)),duration=0.25)  # arrive to password
# # time.sleep(30)
# # pyautogui.click()
