import schedule
import time, os
from activity_tracker import ActivityTracker
from screenshot_manager import ScreenshotManager
from handling_upload import HandlingUpload
from Application import App

def take_screenshot():
    screenshot_manager.capture_screenshot(blurred=False)

if __name__ == "__main__":
    activity_tracker = ActivityTracker()
    screenshot_manager = ScreenshotManager()
    handling_up = HandlingUpload()
    
    # Schedule screenshot every 30 seconds
    app = App(screenshot_manager, handling_up)  # Create an instance of App
    schedule.every(30).seconds.do(take_screenshot)

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
    # Start activity tracking and upload handling in a separate thread
    
    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
