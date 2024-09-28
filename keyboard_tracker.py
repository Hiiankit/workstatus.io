from pynput.keyboard import Listener
import time

class KeyTracker:
    def __init__(self):
        self.i = 0  # Counter for key presses

    def detect_keypress(self):
        start_time = time.time()
        self.i=0
        def press_on(key):
            self.i += 1

        def press_off(key):
            pass  

        # Using Listener to detect key presses and releases
        with Listener(on_press=press_on, on_release=press_off) as listener:
            
            while time.time() - start_time < 5:
                time.sleep(0.1)

            listener.stop() 

        return self.i  # Return the count of key presses after 5 seconds
