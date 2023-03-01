import pyautogui
import keyboard

# Initialize list to store positions of mouse clicks
click_positions = []

# Function to add mouse click positions to the list
def record_click_positions(x, y, button, pressed):
    if pressed and button == 'left':
        click_positions.append((x, y))

# Set up the keyboard shortcut to stop recording
keyboard.add_hotkey('ctrl+alt+s', lambda: keyboard.stop())

# Start recording mouse clicks
pyautogui.onMouseDown(record_click_positions)

# Wait for the keyboard shortcut to stop recording
keyboard.wait()

# Stop recording mouse clicks
pyautogui.onMouseDown(None)

# Print the list of mouse click positions
print("Mouse click positions:")
for position in click_positions:
    print(position)