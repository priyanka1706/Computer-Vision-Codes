import cv2
import numpy as np

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) #eosion then dilation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # dilation then erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) # dilation-erosion
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) #input-opening
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel) #closing-input

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.imshow('erosion', erosion)
cv2.waitKey(0)
cv2.imshow('dilation', dilation)
cv2.waitKey(0)
cv2.imshow('opening', opening)
cv2.waitKey(0)
cv2.imshow('closing', closing)
cv2.waitKey(0)
cv2.imshow('gradient', gradient)
cv2.waitKey(0)
cv2.imshow('tophat', tophat)
cv2.waitKey(0)
cv2.imshow('blackhat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()