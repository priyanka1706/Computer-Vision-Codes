import cv2
import numpy as np

img = cv2.imread('pup.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# OR
# height, width = img.shape[:2]
# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('Orig', img)
cv2.waitKey(0)
cv2.imshow('New', res)
cv2.waitKey(0)

# Translation is the shifting of object’s location.

rows, cols = img.shape[:2]
M = np.float32([[1,0,100],[0,1,50]])
# transform matirix is [[1,0,tx][0,1,ty]]
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Transform', dst)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Rotated', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
