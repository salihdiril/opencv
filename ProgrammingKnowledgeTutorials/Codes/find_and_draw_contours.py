import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Contours can be explained as the curve joining all the continuous points along the boundary which are having the same
# color or intensity. COntours can be useful for shape analysis or object detection or object recognition
# for better accuracy we generally use binary image for finding the contours
# so first we are going to generate binary image and then before finding the contours we are going to apply
# threshold or canny edge detection to find the contours on the image 

img = cv.imread("opencv-logo.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# sometimes the threshold values may be too high so there can be a lot of contours in contours array.
# Hence drawCountours method may not draw contours as a line that covers the edges of the objects inside the image
# Instead it will just draw some points. If we lower the threshold values then everything can be fine
ret, thresh = cv.threshold(imgray, 80, 255, 0)

# findcontours method return two values which are contours and hierarchy
# Parameters: thresh value which we obtain from threshold method, contour mode, method which we going to apply (approximation
# method)
# contours is a Python list of all the contours in the image. Each individual contour is a numpy array of (x,y) coordinates
# of boundary points of the object
# Hierarchy is the optional output vector which is containing the information about image topology 
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(f"Number of contours: {len(contours)}")
print(f"first element of the contours array: {contours[0]}")

# we already fount the contours. Now we need to combine the points of the contour lists to draw contours
# parameters of draw contours method: original image, contours, contours indexes (if we gave -1, the method will draw
# all contours in the contours list), color, thickness
# third parameter is indexes of the found contours. We find 19 contours, so we can give 20 index nums
cv.drawContours(img, contours, -1, (200, 50, 250), 5)

cv.imshow("Image", img)
cv.imshow("Image Gray", imgray)
cv.waitKey(0)
cv.destroyAllWindows()