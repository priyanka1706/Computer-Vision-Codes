# MOG background reduction

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('FG', fgmask)

    k = cv2.waitKey(30) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
