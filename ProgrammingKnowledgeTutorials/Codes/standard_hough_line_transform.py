# The hough transform is a popular technique to detect any shape, if youy can represent that shape in a 
# mathematical form. It can detect the shape even if it is broken or distorted a little
# let's say we have a road image that has lanes in it and we want to detect the lanes.
# first step in order to detect the lane lines in the road is to find the edge pixels using canny edge detection
# or any other edge detection methods. After we find the edge we want to geometrical representation of that edge
# and in order to find geometrical representation of the edge we can use hough transform

# a line in the image space can be expressed with two variables. For example;
# In the cartesian coordinate system: y(i) = mx(i) + c
# In the polar coordinate system: xcos(0) + ycos(0) = r
# when we use cartesian coordinate system, m is the slope of the line and c is the y-intercept of the line
# with hough transform we can represent the line in a different space called mc space instead of xy space
# m will be the x axis and c will be the y axis. So when we represent line in mc space using hough transform
# a line could be represented as a point. In xy space our line is a collection of points and in mc space our line
# is just a point. Hence it will be much more easier for us to do operations with hough transform because we don't have
# to deal with a collection of points.
# so hough transform can transform a line in xy space into a point in mc space and the opposite is also true:
# the hough transform can also transform a line in mc space into a point in xy space.
# line in mc space: c = -x(a)m + y(a) --> -x(a): slope, y(a) = c-intercept
# point in xy space: (x(a), y(a))
# Therefore in xy space we can represent a point as a line in my space and the line's interception will
# be a line in the xy space. 

# polar coordinate system : r = xcos(0) + ysin(0) or y = (-cos(0)/sin(0))*x + r/sin(0)
# so we can represent the line in xy space as a point (r, 0)  in r0 hough space
# we are going to use polar coordinate system generally because cartesian coordinate system format (y(i) = mx(i)+c)
# can't represent vertical lines.

# Hough transform algorithm involves below steps;
#   1-Edge detectin e.g. using the canny edge detector 
#   2-Mapping of edge points to the Hough space and storage in an accumulator
#   3-Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding    
#     and possibly other constraints
#   4-COnversion of infinite lines to finite lines

# Opencv implements two kinds of Hough Line Transforms
# 1-The Standard Hough Transform (HoughLines method)
# 2-The Probabilistic Hough Line Transform (HoughLinesP method)

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# let's say we try to find lines in the sudoku.png image
img = cv.imread("sudoku.png")

# we convert our image to grayscale image because canny edge detector prefers grayscale image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray_img, 50, 150, apertureSize=3)
cv.imshow("Canny Edge", edges)

# parameters: Source: source image
#             Lines: Output vector of lines. Each line is represented by a 2 or 3 element vector (rho, theta) or
#                   (rho, theta, votes). rho is the distance from the coordinate origin (0,0)(top-left corner of the image)
#                   theta is the line rotation angle in radians. votes is the value accumulator
#             Rho: Distance resolution of the accumulator in pixels
#             Theta: Angle resolution of the accumulator in radians
#             Threshold: Accumulator threshold parameter. Only those lines are returned that get enough votes (>threshold)
lines = cv.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    # (x0, y0) gives us the origin or the top-left corner of the image  
    x0 = a*rho
    y0 = b*rho

    # x1 stores the rounded off value of (r*cos(theta) - 1000*sin(theta))
    x1 = int(x0 + 1000*(-b))
    # y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta)))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# the problem is all the lines that we found by hough transform are infinite lines
# this problem can be solved using the other hough method: Probabilistic Hough Line Transform (HoughLinesP method)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()