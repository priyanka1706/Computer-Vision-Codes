import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('template.jpg', 0)
img2 = cv2.imread('match.jpg', 0)

#This is the detector we're going to use for the features.
orb = cv2.ORB_create()
#Here, we find the key points and their descriptors with the orb detector.
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#Here we create matches of the descriptors, then we sort them based on their distances.
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda  x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()
