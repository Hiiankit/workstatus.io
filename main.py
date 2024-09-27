import schedule
import time
from activity_tracker import ActivityTracker
from screenshot_manager import ScreenshotManager

def take_screenshot():
    screenshot_manager.capture_screenshot(blurred=False)

if __name__ == "__main__":
    activity_tracker = ActivityTracker()
    screenshot_manager = ScreenshotManager()
    
    # Schedule screenshot every 10 minutes
    schedule.every(10).minutes.do(take_screenshot)

    # Start activity tracking in a separate thread
    import threading
    activity_thread = threading.Thread(target=activity_tracker.check_activity)
    activity_thread.start()

    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
