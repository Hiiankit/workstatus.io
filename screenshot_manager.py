import pyautogui
import cv2
import os
import time
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class ScreenshotManager:
    def __init__(self , save_dir= None):
        if save_dir is None:
            # Path to Documents/workstatus_screenshots folder
            self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "workstatus_screenshots")
        else:
            self.save_dir = save_dir
    
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        
        # self.delete_ss = DeleteScreenshots()
        # self.delete_ss.delete_all_files()


    def capture_screenshot(self, blurred=False,submit_interval=300):
        while True:
            screenshot = pyautogui.screenshot()
            if blurred:
                screenshot = screenshot.filter(cv2.GaussianBlur((15, 15)))  # Blurring the screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_file = os.path.join(self.save_dir, f"screenshot_{timestamp}.png")
            screenshot.save(screenshot_file)
            print("ss captured")

            time.sleep(submit_interval)
        
        # self.upload_to_s3(screenshot_file)
        # os.remove(screenshot_file)  # Remove local file after upload
