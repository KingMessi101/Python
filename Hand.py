import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw = mp.solutions.drawing.utils
speakers = AudioUtilities.GetSpeakers()
interface = speakers.Activate(IAudioEndpointVolume._iid_, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
minVol, maxVol = volume.GetVolumeRange()[:2]
cap = cv2.VideoCapture(0)

while True:
    success,frame=camera.read()
    if not success:
        break
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLORBGR2RGB)
    results=hands.process(rgb_frame)
    if results.multi_hand_landmarks and results.multi_handedness:
        for i,hand in enumerate(results.multi_hand_landmarks):
            hand_label=results.multi_handedness[i].classification[0].label
            landmarks=hand.landmark
            h,w,_=frame.shape
            thumb=int(landmarks[4].x*w),int(landmarks[4].y*h)
            index=int(landmarks[8].x*w),int(landmarks[8].y*h)
            distance=np.hypot(index[0]-thumb[0],index[1]-thumb[1])
            if hand_label=="left":
                vol=np.interp(distance,[30,300],[minVol,maxVol])
                volume.SetMasterVolumeLevel(vol,None)
            else:
                bright=int(np.interp(distance,[30,300],[0,100]))
                sbc.set_brightness(bright)
            draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Hand Gesture Control",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
camera.release()
cv2.destroyAllWindows()
