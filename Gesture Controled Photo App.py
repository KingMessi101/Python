import cv2, time, numpy as np, mediapipe as mp

hands = mp.solutions.hands.Hands(0.7, 0.7)
draw = mp.solutions.drawing_utils
filters = [None, 'gray', 'sepia', 'neg', 'blur']
f = 0; last = 0; delay = 1

def apply(img, t):
    if t == 'gray': return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if t == 'sepia':
        s = np.array([[.272, .534, .131], [.349, .686, .168], [.393, .769, .189]])
        return np.clip(cv2.transform(img, 5), 0, 225).astype(np.unit)