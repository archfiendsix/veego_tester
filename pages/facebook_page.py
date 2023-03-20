# import logging
# import os
# import pathlib
# import time
# from pathlib import Path
# from turtle import update
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import undetected_chromedriver as ucdriver
# import pyautogui as py
# # import spotipy
# # from spotipy.oauth2 import SpotifyClientCredentials
# import pyautogui
# import pytest
# from selenium.webdriver.support.ui import WebDriverWait
# import selenium
# from selenium.common.exceptions import NoSuchElementException
#
# from selenium.webdriver.chrome.options import Options
#
# import urllib3
# from selenium import webdriver
# #from webdriver_auto_update import check_driver
#
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# driver = ucdriver.Chrome()
# time.sleep(1)
# # driver.get('https://www.facebook.com/')
# # time.sleep(1)
# driver.get('https://www.messenger.com/')
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.XPATH, '//*[@id="email"]').click()
# driver.maximize_window()
# action1 = ActionChains(driver)
# action1.send_keys("veegoveego2019@gmail.com")
# action1.perform()
# driver.implicitly_wait(300)
# # TAB
# action2 = ActionChains(driver)
# action2.send_keys(Keys.TAB)
# action2.perform()
# driver.implicitly_wait(300)
# # Password
# action3 = ActionChains(driver)
# action3.send_keys("veego2019")
# action3.perform()
# driver.implicitly_wait(300)
# time.sleep(1)
# # connect
# action4 = ActionChains(driver)
# action4.send_keys(Keys.ENTER)
# action4.perform()
# driver.implicitly_wait(300)
#
# x = py.size()
# height = x.height
# width = x.width
# center_height = x.height // 2
# center_width = x.width // 2
# py.moveTo(center_width - (width * ( 0.01)), center_height - (height // 4) + (height * ( 0.45)), duration=0.25)
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# # py.moveTo(center_width - (width * (- 0.2990)), center_height - (height // 4) + (height * (- 0.02)), duration=0.25)
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# # py.moveTo(center_width - (width * (0.33)), center_height - (height // 4) + (height * (0.10)),duration=0.25)  # arrive to password
# time.sleep(30)
# pyautogui.click()
