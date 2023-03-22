import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class NexusModsPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10
        self.nav_login_button_locator = (By.CLASS_NAME, "replaced-login-link")
        self.download_button_locator = (By.CSS_SELECTOR, '#slowDownloadButton')

    def nexusmods_signin(self):
        self.driver.maximize_window()

        time.sleep(60)

    def interaction(self, timeout):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.random_scroll(timeout)

    def run_nexusmods_download(self, timeout=180):
        # self.driver.get(self.test_sites["nexusmods_download"])
        # time.sleep(3000)
        self.driver.get("https://supporter-files.nexus-cdn.com/2971/849/Halo%20Reach%20DOOM%20Overhaul-849-1-0-0-1605828697.zip?md5=6EbAi6MBtVGczQaOSjiLkg&expires=1679408959&user_id=175059519&rip=180.195.104.216")
        # self.wait_and_execute(self.driver, self.download_button_locator, 5, lambda elem: elem.click())

        self.logger(f'\nStarting Nexus Mods Download test... \n')

        self.interaction(timeout)
