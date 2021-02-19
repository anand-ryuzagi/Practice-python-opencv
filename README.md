# Practice-python-opencv
A small project to understand the basic operations of opencv module

This project boundes a rectangular outline outside the object having yellow color range and executes some function whenever there is a change in its y axis position.

Module used:

openCV module : (videocapture, cv2.COLOR_BGR2HSV, cv2.inRange(hsv,yellow_lower,yellow_upper),contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE),cv2.contourArea(c),
 cv2.boundingRect(c),cv2.imshow("video",frame))
