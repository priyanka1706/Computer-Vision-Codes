import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('threshold.jpg')
_, t1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, t1, t2, t3, t4, t5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()