import time
import os
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class PCloudMobile(BasePage):
    def __init__(self, mobile_driver, test_sites):
        super().__init__(mobile_driver)
        self.mobile_driver = mobile_driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10
        self.download_button_locator = (By.ID, "com.pcloud.pcloud:id/action_download")
        self.hamburger_button = (By.XPATH, '//android.widget.ImageButton[@content-desc="pCloud"]')
        self.tasks_link = (By.ID, 'com.pcloud.pcloud:id/subtitle')
        self.download_tab = (By.XPATH, '//android.widget.LinearLayout[@content-desc="Download"]/android.widget.TextView')
        self.add_button_locator = (By.ID, 'com.pcloud.pcloud:id/fabs_container')
        self.upload_file_locator = (By.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.ImageButton')
        self.first_file_locator = (By.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView')
        self.select_button_locator = (By.ID, 'com.google.android.documentsui:id/action_menu_select')

    def interaction(self, timeout):
        time.sleep(timeout)

    def run_pcloud_download_mobile(self, timeout=180):
        self.mobile_driver.start_activity("com.pcloud.pcloud", "com.pcloud.screens.Main")
        self.logger('Starting pcloud Download...')
        # Locate the element using its XPATH
        element = self.mobile_driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.ImageButton')

        # Tap on the element
        element.click()

        actions = ActionChains(self.mobile_driver)
        actions.w3c_actions = ActionBuilder(self.mobile_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(495, 1773)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(532, 1305)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        self.wait_and_execute(self.mobile_driver, self.download_button_locator, 10, lambda elem: elem.click())
        self.wait_and_execute(self.mobile_driver, self.hamburger_button, 10, lambda elem: elem.click())
        self.wait_and_execute(self.mobile_driver, self.tasks_link, 10, lambda elem: elem.click())
        self.wait_and_execute(self.mobile_driver, self.download_tab, 10, lambda elem: elem.click())
        self.logger('pCloud Download started...')
        self.interaction(180)

    def run_pcloud_upload_mobile(self, timeout=180):
        self.mobile_driver.start_activity("com.pcloud.pcloud", "com.pcloud.screens.Main")
        self.logger('Starting pcloud Download...')

        self.wait_and_execute(self.mobile_driver, self.add_button_locator, 10, lambda elem: elem.click())
        self.wait_and_execute(self.mobile_driver, self.upload_file_locator, 10, lambda elem: elem.click())
        self.wait_and_execute(self.mobile_driver, self.first_file_locator, 10, lambda elem: elem.click())

        try:
            self.wait_and_execute(self.mobile_driver, self.select_button_locator, 10, lambda elem: elem.click())
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            pass

        self.wait_and_execute(self.mobile_driver, self.hamburger_button, 10, lambda elem: elem.click())
        self.wait_and_execute(self.mobile_driver, self.tasks_link, 10, lambda elem: elem.click())

        self.interaction(timeout)

