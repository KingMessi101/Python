import cv2, numpy as np

def apply_filter(img, f):
    if f == "r":
        img[:, :, 2] = 0
    elif f == "g":
        img[:, :, [0, 2]] = 0
    elif f == "b":
        img[:, :, 1] = 0
    elif f == "s":
        g = cv2.cvtColor(img, 0)
        img = cv2.cvtColor(cv2.Sobel(g, cv2.CV_64F, 1, 0).astype("uint8"))
        cv2.Sobel(g, cv2.CV_64F, 0, 1).astype("uint8")), 8
    elif f == "c":
        img = cv2.cvtColor(
            cv2.Canny(cv2.cvtColor(img, 0), 100, 200), 8)
    elif f == "m":
        g = cv2.medianBlur(cv2.cvtColor(img, 0), 5)
        e = cv2.adaptiveThreshold(g, 255, 0, 0, 9, 9)
        img = cv2.bitwise_and(cv2.bilateralFilter(img, 9, 300, 300), img, mask=0)
    return img
    cap = cv2.VideoCapture(0)
f = ""

print("r,g,b,s,c,t filters | q quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Filter", apply_filter(frame.copy(), f))
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()