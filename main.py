import schedule
import time
from activity_tracker import ActivityTracker
from screenshot_manager import ScreenshotManager
from handling_upload import HandlingUpload
def take_screenshot():
    screenshot_manager.capture_screenshot(blurred=False)

if __name__ == "__main__":
    activity_tracker = ActivityTracker()
    screenshot_manager = ScreenshotManager()
    handling_up = HandlingUpload()
    
    # Schedule screenshot every 30 seconds

    schedule.every(30).seconds.do(take_screenshot)

    # Start activity tracking and upload handling in a separate thread
    import threading
    activity_thread = threading.Thread(target=activity_tracker.check_activity)
    activity_thread.start()
    handling_up_thread = threading.Thread(target=handling_up.upload_to_s3)
    handling_up_thread.start()
    
    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
