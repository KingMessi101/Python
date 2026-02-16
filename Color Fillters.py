import cv2

img = cv2.imread("example.jpg")
if img is None:
    print("Image not found!")
else:
    print("r-Red b-Blue g-Green i+Red d-blue q-Quit")
    while True:
        new = img.copy()
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('r'):
            new[:,:,0] = 0
            new[:,:,1] = 0
        elif key == ord('b'):
            new[:,:,1] = 0
            new[:,:,2] = 0
        elif key == ord('g'):
            new[:,:,2] = cv2.add(new[:,:,2], 50)
        elif key == ord('d'):
            new[:,:,0] = cv2.subtract(new[:,:,0])
        elif key==ord ('q'):
            break
        cv2.imshow("Filltered Image", new)
cv2.destroyAllWindows()