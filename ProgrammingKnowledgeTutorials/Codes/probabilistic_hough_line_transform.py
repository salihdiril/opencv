import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# HoughLineP method is used for probabilistic hough line transformation and it is optimized version of 
# HoughLine method which is used for standard hough line transformation

img = cv.imread("road.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow("Canny", edges)

# we'll use HoughLineP method. It doesn't take all the points. Instead it takes only the random subset of points
# which is sufficient for the line detection
# Parameters: source, rho, theta, threshold, minLineLength(Minimum lenth of line. Line segments shorter than this are 
# rejected), maxLineGap(Maximum allowed gap between line segments to treat them as a single line)

lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:

    # with HoughLineP method we don't have to do a lot of calculation like HoughLine method. HoughLineP method
    # returns two points and we can draw a line with line method    
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1,y1), (x2,y2), (0, 255, 0), 2)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()