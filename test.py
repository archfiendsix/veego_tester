# import telnetlib
#
# # Telnet connection details
# host = '10.0.0.138'
# port = 23
# username = 'Admin'
# password = '142ATJ'
#
# # Connect to the router via Telnet
# tn = telnetlib.Telnet(host, port)
#
# # Read the login prompt
# print(tn.read_until(b"Login: ").decode('ascii'))
#
# # Enter the username
# tn.write(username.encode('ascii') + b"\n")
# print(f"Sent username: {username}")
#
# # Read the password prompt
# print(tn.read_until(b"Password: ").decode('ascii'))
#
# # Enter the password
# tn.write(password.encode('ascii') + b"\n")
# print("Sent password")
#
# # Wait for the command prompt
# print(tn.read_until(b"# ").decode('ascii'))
#
# # Send the 'sh' command
# tn.write(b"sh\n")
# print("Sent 'sh' command")
#
# # Wait for the command prompt
# print(tn.read_until(b"# ").decode('ascii'))
#
# # Send the command to change to the desired directory
# tn.write(b"cd local/veego/agent\n")
# print("Sent 'cd' command")
#
# # Wait for the command to complete
# print(tn.read_until(b"# ").decode('ascii'))
#
# # Send the command to list the files
# tn.write(b"ls\n")
# print("Sent 'ls' command")
#
# # Wait for the command to complete and read the output
# output = tn.read_until(b"# ").decode('ascii')
#
# # Print the output
# print(output)
#
# # Send the command to read the file content
# tn.write(b"cat agent.config.json\n")
# print("Sent 'cat' command")
#
# # Wait for the command to complete and read the output
# output = tn.read_until(b"# ").decode('ascii')
#
# # Print the file content
# print(output)
#
# # Disconnect from the Telnet session
# tn.write(b"exit\n")
# print("Sent 'exit' command")
# tn.close()


##########################################

# import paramiko
#
# #Create SSH Client
# client = paramiko.SSHClient()
#
# #Add SSH Key
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# #Connect to the router
# client.connect(hostname='192.168.210.1', username='root', password=' root')
#
# #Execute commands
# # stdin, stdout, stderr = client.exec_command('pytest C:\\automationVee\\ui\\ui\\tests\\MF\\test_youtube_traffic.py::test_youtube_traffic_only')
# # stdin, stdout, stderr = client.exec_command('driver = ucdriver.Chrome()')
# stdin, stdout, stderr = client.exec_command('ipconfig')
# # stdin, stdout, stderr = client.exec_command('runas /user:administrator regedit; ipconfig')
#
#
# # stdin, stdout, stderr = client.exec_command('./simple_jitter_throttle.sh; 3;1500ms ')
# # # stdin, stdout, stderr = client.exec_command('cd /overlay/work/veego/agent/ ; ./run_veego.sh -qa')
#
# #Read output
# output = stdout.readlines()
#
# #Close connection
# client.close()
#
# print(output)
######################################

import pysftp

# SSH connection details
host = '10.0.0.138'
port = 22
username = 'Admin'
password = '142ATJ'

# Create a connection using pysftp
with pysftp.Connection(host, port=port, username=username, password=password) as sftp:
    # Transfer the file to the router
    local_path = 'agent.config.json'
    remote_path = '/local/veego/agent/agent.config.json'
    sftp.put(local_path, remote_path)

    # Run a command on the router
    command = 'ls -l'
    output = sftp.execute(command)
    print(output)





#
# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.mobileby import MobileBy
#
# # Set up the desired capabilities and initialize the Appium driver
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': '4d791e26',
#     'appPackage': 'com.zhiliaoapp.musically',
#     'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',
#     # Add other desired capabilities as needed
# }
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# # Find an element to swipe on (e.g., a TikTok container)
# tiktok_container = driver.activate_app ("com.zhiliaoapp.musically","com.ss.android.ugc.aweme.splash.SplashActivity")
#
# # Get the dimensions of the container
# container_size = tiktok_container.size
# container_location = tiktok_container.location
# container_width = container_size['width']
# container_height = container_size['height']
# container_x = container_location['x']
# container_y = container_location['y']
#
# # Define the swipe start and end coordinates
# start_x = container_x + container_width * 0.5
# start_y = container_y + container_height * 0.8
# end_x = container_x + container_width * 0.5
# end_y = container_y + container_height * 0.2
#
# # Perform the swipe action
# action = TouchAction(driver)
# action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()
#
# # Add any additional actions or assertions here
#
# # Quit the driver
# driver.quit()