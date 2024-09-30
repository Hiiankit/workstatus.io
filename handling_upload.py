from pynput.keyboard import Listener
import time
import os
import boto3

class HandlingUpload:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        )
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "workstatus_screenshots")
        self.retry_delay = 30

    def upload_to_s3(self):
        """Upload a file to S3, retrying on failure."""
        while True:
            try:
                for file_name in os.listdir(self.save_dir):
                    file_path = os.path.join(self.save_dir, file_name)
                    if os.path.isfile(file_path):  # Check if it's a file
                        self.s3_client.upload_file(file_path, self.bucket_name, file_path)
                        print("file uploaded")
                        os.remove(file_path)  # Delete the file
                        print("file removed")
                time.sleep(100)


                # self.delete_ss.delete_all_files()
            except Exception as e:
                print(f"Upload failed: {e}. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)

    def upload_all(self):
        for file_name in os.listdir(self.save_dir):
                    file_path = os.path.join(self.save_dir, file_name)
                    if os.path.isfile(file_path):  # Check if it's a file
                        self.s3_client.upload_file(file_path, self.bucket_name, file_path)
                        print("file uploaded")
                        os.remove(file_path)  # Delete the file
                        print("file removed")

        