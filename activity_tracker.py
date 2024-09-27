import pyautogui
import time

class ActivityTracker:
    def __init__(self):
        self.active = True
        self.last_mouse_position = pyautogui.position()
    
    def check_activity(self):
        while self.active:
            current_mouse_position = pyautogui.position()
            if current_mouse_position != self.last_mouse_position:
                print("User is active")
            else:
                print("User is inactive")
            self.last_mouse_position = current_mouse_position
            time.sleep(5)  # Check every 5 seconds

    def stop(self):
        self.active = False
