from tkinter import Tk, Button, Label,Entry,IntVar # Tkinter for GUI components
import threading

class App:
    def __init__(self, screenshot_manager, handling_upload):
        self.screenshot_manager = screenshot_manager  # Store screenshot manager instance
        self.handling_upload = handling_upload  # Store handling upload instance
        self.root = Tk()  # Create the main application window
        self.root.title("workstatus.io")  # Set the window title
        
        self.capture_interval_var = IntVar(value=30)  # Default interval of 30 seconds

        self.prompt_label = Label(self.root, text="Enter the screenshot capture interval (in minutes):")
        self.prompt_label.pack(pady=10)  # Add label to the window with padding

        self.interval_entry = Entry(self.root, textvariable=self.capture_interval_var)
        self.interval_entry.pack(pady=30)  # Add Entry widget to the window with padding
        self.interval_entry.insert(0,"")  # Placeholder text

        #  Button to submit capture interval
        self.submit_button = Button(self.root, text="Submit Interval", command=self.submit_interval)
        self.submit_button.pack(pady=10)  # Add button to the window with padding

        # Button to close the application
        self.close_button = Button(self.root, text="Close", command=self.close)
        self.close_button.pack(pady=30)  # Add button to the window with padding

        self.capturing = False  # Initialize capturing flag
        self.capture_thread = None  # Initialize the capture thread to None


        
    def submit_interval(self):
        self.capture_interval = self.capture_interval_var.get()  
        print(f"Capture interval set to {self.capture_interval} seconds.")
        self.interval_entry.config(state="disabled")  # Disable the entry box

        if self.capturing:
            self.capturing = False  # Stop the current loop
            if self.capture_thread is not None:
                self.capture_thread.join()  # Wait for the current thread to finish

        self.capturing = True  # Set the capturing flag to True
        self.start_capturing()  # Start capturing with the new interval

    def start_capturing(self):
        def capture_loop():
            while self.capturing:
                self.screenshot_manager.capture_screenshot(blurred=False, submit_interval=self.capture_interval)
        
        self.capture_thread = threading.Thread(target=capture_loop)
        self.capture_thread.daemon = True  # Make sure thread exits when the program ends
        self.capture_thread.start()

    def close(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
