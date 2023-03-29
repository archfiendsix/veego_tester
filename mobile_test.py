from appium import webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from appium.webdriver import Remote
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerInput
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc_webdriver
import random
import json
import time
import os
import urllib3


from pages.telemetry import Telemetry



# ==============
urllib3.PoolManager(maxsize=10)

chrome_options = uc_webdriver.ChromeOptions()
sessions_dir = os.path.abspath(os.path.join(os.getcwd(), "sessions"))

chrome_options.add_argument(f"--user-data-dir={sessions_dir}")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-beforeunload")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-session-crashed-bubble")

chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1,
    "credentials_enable_service": 1
})
config_dir = os.path.abspath(os.path.join(os.getcwd(), "config.json"))
with open(config_dir, "r") as json_file:
    config_data = json.load(json_file)

bdriver = uc_webdriver.Chrome(options=chrome_options)
telemetry = Telemetry(bdriver, config_data)
# prefs = {"download.default_directory": download_dir}
# chrome_options.add_experimental_option("prefs", prefs)
sessions_dir = os.path.abspath(os.path.join(os.getcwd(), "sessions"))
# sessions_dir = os.path.abspath(os.path.join(os.path.expanduser("~"), ".chrome_sessions"))
# Create the folder if it doesn't already exist
os.makedirs(sessions_dir, exist_ok=True)
for session_file in os.listdir(sessions_dir):
    if session_file.endswith(".session"):
        with open(os.path.join(sessions_dir, session_file), "r") as f:
            cookie_data = f.read().strip().split("\n")
            cookies = {}
            for line in cookie_data:
                name, value, domain, path, expires, secure, http_only = line.split("\t")
                cookies[name] = {
                    "value": value,
                    "domain": domain,
                    "path": path,
                    "expires": expires,
                    "secure": secure,
                    "httpOnly": http_only
                }
            for cookie in cookies.values():
                bdriver.add_cookie(cookie)









#==========

desired_caps = {
    "automationName":"UIAutomator2",
  "deviceName": "477cffc9",
  "platformName": "Android",
    "platformVersion": "13",
  # "appPackage": "com.zhiliaoapp.musically",
  # "AppActivity": "com.zhiliaoapp.musically.MainActivity",
  # "app": "C:\\Users\\Ace\\Desktop\\Wrk\\veego_tester\\TikTok_28.9.1_Apkpure.apk"
    # "appium:ignoreHiddenApiPolicyError ": True,
    "noReset":True
}




# options = Options()
# options.set_capability('automationName', 'UIAutomator2')
# options.set_capability('deviceName', '477cffc9')
# options.set_capability('platformName', 'Android')
# options.set_capability('platformVersion', '13')
# options.set_capability('app', 'C:\\Users\\Ace\\Desktop\\Wrk\\veego_tester\\TikTok_28.9.1_Apkpure.apk')


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# driver = Chrome(executable_path='./chromedriver', options=chrome_options)
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# driver = Remote('http://localhost:4723/wd/hub', options.to_capabilities())

# ==========================
# driver.start_activity("com.ss.android.ugc.trill","com.ss.android.ugc.aweme.splash.SplashActivity")
#
#
# # Get the dimensions of the screen
# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']
#
# start_time = time.time()
# timeout = 20
#
# while time.time() - start_time < timeout:
#     # Wait for a random time between 0 and 10 seconds
#     time.sleep(random.randint(0, 5))  # wait for n seconds between scrolls
#
#     # Calculate the start and end coordinates for the swipe
#     start_x = width / 2
#     start_y = height / 2
#     end_x = start_x
#     end_y = start_y - (height * 0.1)  # move in the opposite direction
#
#     # Perform the swipe action
#     action = TouchAction(driver)
#     action.press(x=start_x, y=start_y).wait(200).move_to(x=end_x, y=end_y).release().perform()
# ==========================

driver.start_activity("com.pcloud.pcloud", "com.pcloud.screens.Main")

# Locate the element using its XPATH
element = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.ImageButton')

# Tap on the element
element.click()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(495, 1773)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(532, 1305)
actions.w3c_actions.pointer_action.release()
actions.perform()


download_element = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[9]/android.widget.CheckedTextView")
download_element.click()
time.sleep(180)
telemetry.run_telemetry_test("pCloud", "DOWNLOAD", True)

driver.quit()
