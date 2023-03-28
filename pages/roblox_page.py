from selenium.webdriver.common.by import By
import os
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class RobloxPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_roblox_game(self, timeout):
        self.driver.get(
            self.test_sites['roblox_gaming'])
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="game-details-play-button-container"]/button').click()
        time.sleep(1)
        self.logger("Roblox conferencing started...")
        self.interaction(timeout)




# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#     driver = ucdriver.Chrome()
#     time.sleep(1)
#     driver.get('https://www.roblox.com/games/2830250344/Horse-Valley')
#     driver.maximize_window()
#     driver.implicitly_wait(300)
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="right-navigation-header"]/div[2]/ul/li[2]/a').send_keys(Keys.ENTER)
#     driver.implicitly_wait(300)
#     time.sleep(2)
#     driver.find_element(By.XPATH, '// *[ @ id = "login-username"]').click()
#
#     action1 = ActionChains(driver)
#     action1.send_keys("RihannaPiskael")
#     action1.perform()
#     driver.implicitly_wait(300)
#     # TAB
#     action2 = ActionChains(driver)
#     action2.send_keys(Keys.TAB)
#     action2.perform()
#     driver.implicitly_wait(300)
#     # Password
#     action3 = ActionChains(driver)
#     action3.send_keys("RihannaPiskael1")
#     action3.perform()
#     driver.implicitly_wait(300)
#     time.sleep(1)
#     # connect
#     action4 = ActionChains(driver)
#     action4.send_keys(Keys.ENTER)
#     action4.perform()
#     driver.implicitly_wait(300)
#     time.sleep(3)
#
#     x = py.size()
#     height = x.height
#     width = x.width
#     center_height = x.height // 2
#     center_width = x.width // 2
#     py.moveTo(center_width - (width * (0.2990)), center_height - (height // 4) + (height * (0.2)), duration=0.25)
#     time.sleep(2)
#     pyautogui.click()
#     time.sleep(2)
#     py.click()
#     action4 = ActionChains(driver)
#     action4.send_keys(Keys.ENTER)
#     action4.perform()
#     time.sleep(2)
#     pyautogui.click()
#
#     x = py.size()
#     height = x.height
#     width = x.width
#     center_height = x.height // 2
#     center_width = x.width // 2
#     time.sleep(2)
#     py.moveTo(center_width - (width * (0.2)), center_height - (height // 4) + (height * (0.5)),duration=0.25)  # Confirmation to sync
#     time.sleep(2)
#     pyautogui.click()
#     pyautogui.click()
#     time.sleep(2)
#     py.moveTo(center_width - (width * (- 0.16)), center_height - (height // 4) + (height * (0.5)),duration=0.25)  # arrive to icon of user in chrome
#     # driver.implicitly_wait(200)
#     time.sleep(2)
#     pyautogui.click()
#     pyautogui.click()
#     time.sleep(2)
#     # py.moveTo(center_width - (width * (- 0.0090)), center_height - (height // 4) + (height * (0.42)), duration=0.25)
#     time.sleep(2)
#     pyautogui.click()
#     py.click()
#     time.sleep(2)
#     # driver(os.close)
#     py.moveTo(center_width - (width * (0.03590)), center_height - (height // 4) + (height * (0.05)), duration=0.25) #open roblox
#     # py.moveTo(center_width - (width * (-0.01)), center_height - (height // 4) + (height * (0.33)),duration=0.25)  # arrive to icon of user in chrome
#     # driver.implicitly_wait(200)
#     time.sleep(2)
#     pyautogui.click()
#     # pyautogui.click()
#     time.sleep(20)
#     py.moveTo(center_width - (width * (- 0.47)), center_height - (height // 4) + (height * (0.2)), duration=0.25)
#
#     time.sleep(5)
#     pyautogui.click()
#     pyautogui.press('enter')
#     # pyautogui.click()
#     # pyautogui.click()
#     py.click()
#     # time.sleep(2)
#     action = ActionChains(driver)
#     action.send_keys(Keys.ENTER)
#     action.perform()
#     # driver.implicitly_wait(300)
#     time.sleep(4)
#     py.moveTo(center_width - (width * ( -0.07)), center_height - (height // 4) + (height * (0.26)), duration=0.25)
#     pyautogui.click()
#     pyautogui.press('enter')
#     pyautogui.write('Hello world!', interval=0.25)
#     # pyautogui.click()
#     time.sleep(15)