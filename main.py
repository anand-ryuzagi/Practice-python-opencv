import cv2
import numpy as np

yellow_lower = np.array([22,93,0])
yellow_upper = np.array([45,255,255])

capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
prev_y = 0

while True:
    isTrue, frame = capture.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,yellow_lower,yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:
            # cv2.drawContours(frame, c, -1, (0,255,0), 2)
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if y < prev_y:
                print("moving down")
            prev_y = y
    cv2.imshow("video",frame)
    # cv2.imshow("hsv",hsv)
    cv2.imshow("mask",mask)
    if cv2.waitKey(50) & 0xff==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()