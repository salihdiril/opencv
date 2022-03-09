import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# previously we have learned that how we detect lines using hough transformation
# in this program we'll learn how to find circles using hough transformation

img = cv.imread("shapes.png")
output = np.copy(img)
# hough circle transform works like below;
# (x_center, y_center) is the center of the circle, and r is the radius of the circle
# (x - x_center)^2 + (y - y_center)^2 = r^2 : Circle's mathematical representation
# our hough circle method will work grayscale and blurred image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)

# houghcircles method takes a few parameters:
    # source: 8-bit image, single-channel, grayscale input image
    # circles: output vector of found circles
    # method: detection method, see HoughModes. Currently, the only implemented method is HOUGH_GRADIENT
    # dp: inverse ratio of the accumulator resolution to the image resolution
    # minDist: Minimum distance between the centers of the detected circles
    # param1: first method-specific parameter. In case of HOUGH_GRADIENT, it is higher threshold of the two passed
    #       to the Canny Edge Detector (the lower one is twice smaller)
    # param2: Second method-specific  parameter. In case of HOUGH_GRADIENT, it is the accumulator threshold for the
    #       circle centers at the detection stage
    # minRadius: minimum circle radius
    # maxRadius: Maximum circle radius. if <= 0, uses the max image dimension, if < 0, returns center without
    #           finding the radius
# houghCircle method will give us a circle vector which we can iterate upon but first of all we need to convert
# those circle parameters which we got using the circles variables that is x and y coordinate and radius into an integer
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (255, 255, 255), thickness=3)
    cv.circle(output, (x, y), 2, (0, 255, 255), thickness=3) # this will draw a dot




 
cv.imshow("output", output)
cv.waitKey(0)
cv.destroyAllWindows()