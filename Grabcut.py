# Initially user draws a rectangle around the foreground region (foreground region should be completely inside the rectangle).
# Then algorithm segments it iteratively to get the best result. Done. But in some cases, the segmentation won't be fine,
# like, it may have marked some foreground region as background and vice versa. In that case, user need to do fine touch-ups.
# Just give some strokes on the images where some faulty results are there. Then in the next iteration, you get better results.

# https://docs.opencv.org/trunk/d8/d83/tutorial_py_grabcut.html

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pup.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

# These are arrays used by the algorithm internally. You just create two np.float64 type zero arrays of size (1,65).
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#The real important part is the rect we define. This is rect = (start_x, start_y, width, height).
rect = (120,10,350,170)
#    cv2.rectangle(img, (120,10), (350,170), (200,100,150), 5)
#    cv2.imshow('Pup', img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

#  First the input image, then the mask, then the rectangle for our main object, the background model, foreground model,
#  the amount of iterations to run, and what mode you are using.
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
# the mask is changed so that all 0 and 2 pixels are converted to the background, where the 1 and 3 pixels are now the foreground.
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()