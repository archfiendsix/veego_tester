import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='function')
def driver(request):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Your Device ID',
        'appPackage': 'com.zhiliaoapp.musically',
        'appActivity': 'com.zhiliaoapp.musically.MainActivity',
        'automationName': 'UiAutomator2',
        'noReset': True,
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver

def test_open_tiktok(driver):
    # Wait for TikTok to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((MobileBy.ID, 'com.zhiliaoapp.musically:id/bottom_tab_button_home'))
    )
    print("TikTok app opened successfully.")
