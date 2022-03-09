import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# the canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide 
# range of edges in images. It was developed by John F. Canny in 1986
# THe Canny Edge Detection algorithm is composed of 5 steps:
# 1-Noise reduction (Apply gaussian filter to smooth the image and remove noise)
# 2-Gradient Calculation (find the intensity gradience of the image)
# 3-Non-maximum Suppression (to get rid of unwanted response to edge detection)
# 4-DOuble Threshold (to determine potential edges)
# 5-Edge tracking by Hysteresis (finalize the detection of the edges by suppressing all the other edges that are weak or
# not connected to strong edges)

def nothing(x):
    pass

img = cv.imread("messi5.jpg", 0)
cv.namedWindow("image")

# let's apply canny edge detection method
# parameters: source, first threshold value, second threshold value (these 2 values for hysteresis procedure)
# we can add trackbar to control the threshold values
cv.createTrackbar("threshold1 value controller", "image", 0, 255, nothing)
cv.createTrackbar("threshold2 value controller", "image", 0, 255, nothing)

while True:

    threshold1 = cv.getTrackbarPos("threshold1 value controller", "image")
    threshold2 = cv.getTrackbarPos("threshold2 value controller", "image")

    canny = cv.Canny(img, threshold1, threshold2)
    titles = ["image", "Canny"]
    images = [img, canny]
    
    cv.imshow("image2", images[0])
    cv.imshow("image", images[1])

    k = cv.waitKey(1) & 0xFF 
    if k == 27:
        break

cv.destroyAllWindows()