import cv2, time, pyautogui
import mediapipe as mp
hands = mp.solutions.hands.Hands(max_num_hands = 1, min_detection_confidence = 0.7)
draw = mp.solutions.drawing_utils
def gesture(lm, hand):
    tips = [8, 12, 16, 20]
    fingers = [1 for t in tips if lm.landmark[t].y< lm.landmark[t - 2].y]
    thumb = lm.landmark [4]
    thumb_ip = lm.landmark [3]
    if(hand=="Right" and thumb.x>thumb_ip.x) or (hand=="Left" and thumb.x<thumb_ip.x):
        fingers.append(1)
    if len(fingers)==5:
        return "up"
    if len(fingers)==0:
        return "down"

cap = cv2.VideoCapture(0)
last = 0
while cap.isOpened():
    ok, img = cap.read()
    if not ok:
        break
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
    res = hands.process(img)
    g = "none"

    if res.multi_hand_landmarks:
        for h, info in zip(res.multi_hand_landmarks.res.multi_handedness):
            hand = info.classification[0].label
            g=gesture(h, hand)
            draw.draw_landmarks(img, h, mp.solutions.hand.HAND_CONECTIONS)
            if time.time-last>1:
                if g =="up":
                    pyautogui.scroll(300)

                if g =="down":
                    pyautogui.scroll(-300)
                    last = last.time()
    cv2.imshow("Gesture Scroll", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()