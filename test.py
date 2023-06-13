# import pyautogui
# import keyboard
#
# # Initialize list to store positions of mouse clicks
# click_positions = []
#
# # Function to add mouse click positions to the list
# def record_click_positions(x, y, button, pressed):
#     if pressed and button == 'left':
#         click_positions.append((x, y))
#
# # Set up the keyboard shortcut to stop recording
# keyboard.add_hotkey('ctrl+alt+s', lambda: keyboard.stop())
#
# # Start recording mouse clicks
# pyautogui.onMouseDown(record_click_positions)
#
# # Wait for the keyboard shortcut to stop recording
# keyboard.wait()
#
# # Stop recording mouse clicks
# pyautogui.onMouseDown(None)
#
# # Print the list of mouse click positions
# print("Mouse click positions:")
# for position in click_positions:
#     print(position)


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy

# Set up the desired capabilities and initialize the Appium driver
desired_caps = {
    'platformName': 'Android',
    'deviceName': '4d791e26',
    'appPackage': 'com.zhiliaoapp.musically',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',
    # Add other desired capabilities as needed
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Find an element to swipe on (e.g., a TikTok container)
tiktok_container = driver.activate_app ("com.zhiliaoapp.musically","com.ss.android.ugc.aweme.splash.SplashActivity")

# Get the dimensions of the container
container_size = tiktok_container.size
container_location = tiktok_container.location
container_width = container_size['width']
container_height = container_size['height']
container_x = container_location['x']
container_y = container_location['y']

# Define the swipe start and end coordinates
start_x = container_x + container_width * 0.5
start_y = container_y + container_height * 0.8
end_x = container_x + container_width * 0.5
end_y = container_y + container_height * 0.2

# Perform the swipe action
action = TouchAction(driver)
action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()

# Add any additional actions or assertions here

# Quit the driver
driver.quit()