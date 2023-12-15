import cv2
import time
import datetime
import os

stream_url = "http://localhost:8080/?action=stream"

today = datetime.date.today().strftime("%Y%m%d")

folder_name = f"/app/images/{today}"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

cap = cv2.VideoCapture(stream_url)

while True:
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        cv2.imwrite(os.path.join(folder_name, f"frame_{timestamp}.jpg"), frame)
        time.sleep(0.2)
    else:
        break

cap.release()
