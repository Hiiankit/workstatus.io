import subprocess
import sys

import schedule
import time, os
from activity_tracker import ActivityTracker
from screenshot_manager import ScreenshotManager
from handling_upload import HandlingUpload
from Application import App
#install all the required packages 
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = [
    "pyautogui",
    "opencv-python",
    "boto3",
    "python-dotenv",
]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)
    
def take_screenshot():
    screenshot_manager.capture_screenshot(blurred=False)

if __name__ == "__main__":
    activity_tracker = ActivityTracker()
    screenshot_manager = ScreenshotManager()
    handling_up = HandlingUpload()
    
    # Schedule screenshot every 30 seconds
    app = App(screenshot_manager, handling_up)  # Create an instance of App
    # schedule.every(30).seconds.do(take_screenshot)

    import threading
    activity_thread = threading.Thread(target=activity_tracker.check_activity)
    activity_thread.start()
    handling_up_thread = threading.Thread(target=handling_up.upload_to_s3)
    handling_up_thread.start()
    # screenshot_manager_thread = threading.Thread(target=screenshot_manager.capture_screenshot)
    # screenshot_manager_thread.start()

    app.run()

    handling_up.upload_all()

    os._exit(0)
    
    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
