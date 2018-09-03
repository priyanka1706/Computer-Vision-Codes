import cv2
import numpy as np
import time


img = cv2.imread('pup.jpg')
px = img[200][200]
print(px)

#for i in range(110,130):
#    for j in range(220,250):
#        img[i][j] = [255,0,0]

# can call seperately for BGR values
k =img.item(200,200,2)
print(k)
print(img.shape)
print(img.size)
print(img.dtype)

#copying nose
nose = img[110:130, 220:250]
img[270:290, 370:400] = nose

b,g,r = cv2.split(img)
# b = img[:,:,0]
# img[:,:,2] = 0
# cv2.imshow('Blue pup', b)
img = cv2.merge((b,g,r))
#constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value='BLUE')

ev1 = time.time() #cv2.getTickCount()
img2 = cv2.imread('cv.png')

rows,cols,channels = img2.shape
print(img2.shape)
roi = img[0:rows, 0:cols ]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
print(mask_inv.shape)

#background
# mask sent here mjst be white bg with black logo
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

#foreground
# here must be black bg with white logo  
img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)

dst = cv2.add(img1_bg,img2_fg)
img[0:rows, 0:cols ] = dst

cv2.imshow('gray', mask)
cv2.waitKey(0)

cv2.imshow('gray', img1_bg)
cv2.waitKey(0)

cv2.imshow('gray', mask_inv)
cv2.waitKey(0)

cv2.imshow('gray', img2_fg)
cv2.waitKey(0)

cv2.imshow('gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ev2 = time.time()#cv2.getTickCount()
print((ev2-ev1))#/cv2.getTickFrequency())
print(cv2.useOptimized())