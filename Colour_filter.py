# How to find a colour filter
# green = np.uint8([[[0,255,0 ]]])
# hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print hsv_green
# [[[ 60 255 255]]]

# This code is for a colour filter for pink
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv = hue, saturation, value
    # hue is super important
    # tweak this accordingly
    lower_pink = np.array([50,50,70])
    upper_pink = np.array([255,255,255])

    # when in the range, it will be white, where not 0
    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    # where there are 1sin our mask,  it will show color from the frame
    res = cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((15,15), np.float32)/225 #average filter
    smoothed = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15,15), 0) # Gaussian blur

    median = cv2.medianBlur(res, 15) #median blue, probs the best

    bilateral = cv2.bilateralFilter(res, 15, 75, 75) #bilateral blur

    # cv2.imshow('Frame', frame)
    # cv2.imshow('Result', res)
    cv2.imshow('Smoothed', smoothed)
    cv2.imshow('Blur', median)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()