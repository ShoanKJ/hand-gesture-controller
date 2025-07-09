import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detect = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 400)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detect.findHands(img) 

    if hands and hands[0]["type"] == "Left":
        fingers = detect.fingersUp(hands[0])
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50), 
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if totalFingers==5:
            pyautogui.keyDown("right")
            pyautogui.keyUp("left")
        if totalFingers==0:
            pyautogui.keyDown("left")
            pyautogui.keyUp("right")    

    cv2.imshow('Camera Feed', img)  

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
