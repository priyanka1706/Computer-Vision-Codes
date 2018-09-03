import numpy as np
import cv2
import matplotlib.pyplot as plt
# Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the
# shape. default thickness = 1

# BGR
img = np.zeros((512, 512, 3), np.uint8)

# line thickness 5
cv2.line(img, (0,0), (511,511), (255,0,0), 5)

# plt.imshow(img)
# plt.xticks([]), plt.ylabel([])
# plt.show()

# you need top-left corner and bottom-right corner of rectangle
cv2.rectangle(img, (384,0), (510,128), (0,0,255), 3)

#  you need its center coordinates and radius
cv2.circle(img, (447, 63), 63, (0,255,0), -1)

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[100,50],[140,200],[270,250],[340,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# To put texts in images, you need specify following things.
# Text data that you want to write
# Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
# Font type (Check cv2.putText() docs for supported fonts)
# Font Scale (specifies the size of font)
# regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 3,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
