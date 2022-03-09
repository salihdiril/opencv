import numpy as np
import cv2 as cv

# with simple thresholding we set a global threshold value and all the pixels of the input image
# is compared with that value. In this program we'll learn how to use adaptive thresholding
# In adaptive thresholding, we set a threshold value according to the different regions of the input image
# Hence there will be no global threshold value.
# We use adaptive thresholding instead of simple thresholding in case of varying illumination in the image

img = cv.imread("sudoku.png", 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# now let's use adaptive thresholding
# adaptive threshold method takes several arguments
# first one is source, secon one is maxvalue which is the non-zero value assigned to the pixels for which
# the condition is satisfied. In our case it is 255. We can't give higher value than 255 to a pixel.
# Third parameter is the adaptive method. Adaptive method decides how the threshold value will be calculated
# There are two types of adaptive methods. First one is adaptive_thresh_mean_c. This means threshold value will
# be the mean of the neighborhood area. The secon type of adaptive method is adaptive_thresh_gaussian_c. This means
# threshold value will be the weighted sum  of the neighborhood area.
# Fourth parameter will be the threshold type.
# fifth argument is blocksize. This will decide the neighborhood area.
# sixth argument is the C value inside the adaptive methods that will be subtracted 
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) 
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) 

cv.imshow("image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)

cv.waitKey(0)
cv.destroyAllWindows()