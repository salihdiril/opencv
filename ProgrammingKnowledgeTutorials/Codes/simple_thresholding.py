import numpy as np
import cv2 as cv

# Thresholding is a very popular segmentation technique used for seperating an object from its background
# The process of thresholding involves comparing each pixel of an image with a pre-defined threshold value
# and this type of comparison of each pixel of an image to a threshold value divides all the pixels 
# of the input image into two groups. So the first group involves having intensity value lower than the threshold
# value and the second group involves the pixels having intensity value greater than the threshold value

img = cv.imread("gradient.png", 0)

# thresholding function return "ret" value and thresholded value of an image
# threshold values takes several arguments
# first one is source, second one is a threshold value, third one is the max value of threshold
# and the fourth one is threshold type. There are several types in simple thresholding
# the first one is Threshold_binary
# threshold binary simple thresholding technique will compare threshold value with each pixel of the input image
# and if the pixel value greater than the threshold value, the technique will set that pixel as 1. Otherwise
# it will set it as 0. So the image will become a black and white image
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# now let's look at the other type of thresholding technique.
# this technique is called as Thresh_binary_inverse
# this technique will give us the inverse result of the thresh_binary 
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

# next thresholding technique is thresh_trunc
# up to the threshold value the thresholded image's pixel values will not change
# After the threshold value the pixels having greater value than threshold value will have the same value
# with the threshold value.
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# the other thresholding technique is thresh_tozero
# This technique makes the pixels having value less than the threshold value 0 and let the pixels having greater value
# than the threshold value have their own value.
_, th4 = cv.threshold(img, 23, 255, cv.THRESH_TOZERO)

# thresg_tozero_inv is working with opposite principle of the thresh_tozero
# It makes the pixels greater than the threshold value zero and do nothing about others
_, th5 = cv.threshold(img, 23, 255, cv.THRESH_TOZERO_INV)

cv.imshow('image', img)
cv.imshow('thresholded image by thresh_binary', th1)
cv.imshow('thresholded image by thresh_binary_inv', th2)
cv.imshow('thresholded image by thresh_trunc', th3)
cv.imshow('thresholded image by thresh_tozero', th4)
cv.imshow('thresholded image by thresh_tozero_inv', th5)

cv.waitKey(0)
cv.destroyAllWindows() 

