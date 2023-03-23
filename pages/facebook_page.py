from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class FacebookPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites

    def facebook_signin(self):
        self.driver.switch_to.default_content()

        # self.wait_and_execute(
        #     self.driver, (By.CSS_SELECTOR, 'a[data-testid="loginButton"]'), 10, lambda elem: elem.click())
        # time.sleep(3000)
        self.wait_and_execute(
            self.driver, (By.CSS_SELECTOR, 'input[autocomplete="username"]'), 5,
            lambda elem: elem.send_keys(self.env_facebook_email))

        self.wait_and_execute(
            self.driver, (By.XPATH, "//span[contains(text(), 'Next')]"), 5,
            lambda elem: elem.click())

        self.wait_and_execute(
            self.driver, (By.CSS_SELECTOR, 'input[type="password"]'), 5,
            lambda elem: elem.send_keys(self.env_facebook_password))

        self.wait_and_execute(
            self.driver, (By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]'), 5, lambda elem: elem.click())

    def interaction(self, timeout=180):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.random_scroll(timeout)

    def run_facebook_social(self, timeout=180):

        self.driver.get(self.test_sites["facebook_social"])

        try:
            signin_iframe_locator = (By.CSS_SELECTOR, 'iframe[title="Sign in with Google Dialog"]')
            signin_iframe = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    signin_iframe_locator)
            )

            self.driver.switch_to.frame(signin_iframe)

            continue_as = (By.CSS_SELECTOR, '#continue-as')

            self.wait_and_execute(self.driver, continue_as, 5, lambda elem: elem.click())
        except(NoSuchElementException, TimeoutException):
            pass

        # self.twitter_signin(self.env_facebook_email, self.env_facebook_password)
        self.logger(f'\nRunning Facebook Social... \n')
        self.interaction(timeout)


'''
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
driver = ucdriver.Chrome()
# ucdriver.add_argument("--disable-extensions")
action = ActionChains(driver)

driver.get('https://us05web.zoom.us/s/7383420305?pwd=YVRLUmo2RUc4bmNzMGNlWmVGeDNoQT09#success')
driver.maximize_window()
driver.implicitly_wait(300)  # Accept cookies
driver.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/a').click()
driver.implicitly_wait(300)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
driver.implicitly_wait(300)  # sign In
driver.find_element(By.XPATH,
                    '// *[ @ id = "app"] / div / div[2] / div / div[1] / form / div[1] / div / div[1] / label').click()
driver.implicitly_wait(300)
time.sleep(1)  # userName
action1 = ActionChains(driver)
action1.send_keys("veegoQA@gmail.com")
action1.perform()
driver.implicitly_wait(300)
# TAB
action2 = ActionChains(driver)
action2.send_keys(Keys.TAB)
action2.perform()
time.sleep(1)
driver.implicitly_wait(300)  # Password
action3 = ActionChains(driver)
action3.send_keys("QA123456789qa")
action3.perform()
driver.implicitly_wait(400)
time.sleep(3)  # Push on "Sign In"
driver.find_element(By.XPATH, '//*[@id="js_btn_login"]/span').click()
driver.implicitly_wait(300)
time.sleep(1)  # crashing!!
# driver.find_element(By.XPATH, '// *[ @ id = "zoom-ui-frame"] / div[2] / div / div[1] / div"]').click()
# time.sleep(1)
time.sleep(10)

x = py.size()
height = x.height
width = x.width
center_height = x.height // 2
center_width = x.width // 2
py.moveTo(center_width - (width * (- 0.0090)), center_height - (height // 4) + (height * (0.42)), duration=0.25)
time.sleep(5)
pyautogui.click()
py.click()
time.sleep(20)
# driver(os.close)
py.moveTo(center_width - (width * (0.03590)), center_height - (height // 4) + (height * (0.05)), duration=0.25)
time.sleep(5)
pyautogui.click()
py.click()

'''