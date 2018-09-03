import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_pink = np.array([50,50,70])
    upper_pink = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    #  The goal with opening is to remove "false positives" so to speak. Sometimes, in the background, you get some pixels
    # here and there of "noise." The idea of "closing" is to remove false negatives. Basically this is where you have your
    # detected shape, like our hat, and yet you still have some black pixels within the object. Closing will attempt to clear
    # that up.
    #opening removes false positives, closing removes false negati es
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    # cv2.imshow('Frame', frame)
    # cv2.imshow('Result', res)
    # cv2.imshow('erosion', erosion)
    # cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()



