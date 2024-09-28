import pyautogui
import cv2
import os
import boto3
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class ScreenshotManager:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        )
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")

    def capture_screenshot(self, blurred=False):
        screenshot = pyautogui.screenshot()
        if blurred:
            screenshot = screenshot.filter(cv2.GaussianBlur((15, 15)))  # Blurring the screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_file = f"screenshot_{timestamp}.png"
        screenshot.save(screenshot_file)
        self.upload_to_s3(screenshot_file)
        os.remove(screenshot_file)  # Remove local file after upload

    def upload_to_s3(self, filename):
        self.s3_client.upload_file(filename, self.bucket_name, filename)
        print(f"Uploaded {filename} to S3")

