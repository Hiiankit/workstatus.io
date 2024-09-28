import pyautogui
import time
from keyboard_tracker import KeyTracker


class ActivityTracker:
    def __init__(self):
        self.active = True
        self.last_mouse_position = pyautogui.position()
        self.key_counter = KeyTracker()       
    
    def check_activity(self):
        while self.active:
            current_mouse_position = pyautogui.position()
            pressed = self.key_counter.detect_keypress()

            if current_mouse_position != self.last_mouse_position or pressed > 0:
                print("User is active")
            else:
                print("User is inactive")
            self.last_mouse_position = current_mouse_position
            # time.sleep(5)  # Check every 5 seconds

    def stop(self):
        self.active = False
