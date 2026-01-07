import cv2
import cv2, numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: webcam not found")
    exit()

lower_skin = np.array([0, 20, 70], np.uint8)
upper_skin = np.array([20, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
if contours:
    cnt = nax(contours, )