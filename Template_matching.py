import cv2
import numpy as np

img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# We specify a threshold, here 0.8 for 80%.
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)

# lowering threshold gives false posiives
# one way of getting less false positives is inc threshold, like 90-100%
# Another option would be to just take another template image. Sometimes, it can be useful to have multiple images of the
# same object. This way, you can keep your threshold high enough to be relatively certain that your results will be accurate.