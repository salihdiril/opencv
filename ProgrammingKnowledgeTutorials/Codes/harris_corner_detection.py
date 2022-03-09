import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# In this program we try to understand how we can find out the corners inside an image using a method called
# harris corner detection.
# Now first of all what is a corner. Corners are the region in the image with large variation in intensity in all
# the direction. Detecting corners using harris corner detection contains three main steps;
    # 1 - Determine which windows produce very large variations in intensity when moved in both X and Y direction
        # windows: In this case window is a small rectangle inside the image where you look. You search a very
        #       large variation in intensity in that small rectangle both vertical and horizontal direction.
    # 2 - with each such window found, a score R is computed
    # 3 - After applying a threshold to this score, important corners are selected & marked

# mathematical operations behind the 1. step is;
# E(u,v) = sum, sigma (x,y) [w(x,y)(window function) I(x+u, y+v)(shifted intensity) - I(x,y)(intensity)]^2]
# so the above operation means that we have a pixel that has the coordinates x and y and that pixel is the center of
# our window. We shift our window by u pixel horizontally and v pixel vertically. first we find our original window's
# center's (x,y) intensity and then we find the shifted window's center's (x+u, y+v) intensity. We calculate the difference
# and then calculate its square. Then we do the same operations with the next window which is obtained by augmenting x and y
# Finally we sum up all the founded values and acquire a score and that score is E(u,v)
# Our goal is to maximize this E(u,v) to find the edges. We need to do Taylor Expansion to create a formula
# that gives us a E(u,v) which has the greatest score. 
# E(u,v) = [u,v]M[u] --> M[u] = sigma(x,y)[w(x,y) [I(x)I(x)  I(x)I(y)]]
#                [v]      [v]                     [I(x)I(y)  I(y)I(y)]  
# I(x) and I(y)'s are image derivatives in the x and y directions respectively

# mathematical operations behind the 2. steps is;
# we calculate the score R. R = det(M) - k(trace(M))^2
# where, det(M) = lambda(1)*lambda(2), trace(M) = lambda(1) + lambda(2) and lambda(1) and lambda(2) are the eigen values of M
# M is already found in the first step. 
# Eigenvalues --> AV = lambda*V where V is a vector and A is a matrix and lambda is a scalar
# AV = lambda*V --> (A-lambda*I)V=0 where I is identity matrix

# mathematical operations behind the 3. step is;
# abs(R) is small, which happens when lambda(1) and lambda(2) are small, the region is flat
# R<0, which happens when lambda(1)>>lambda(2) or vice versa, the region is edge
# R is large, which happens when lambda(1) and lambda(2) are large and lambda(1) ~ lambda(2), the region is a corner

img = cv.imread("chessboard.png")
img = cv.resize(img, (512, 512))

cv.imshow("image", img)

# Because cornerHarris method works with grayscale image in float32 format, we convert our image to grayscale float32 format
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

# cornerHarris method takes a few arguments
# Parameters: source, blocksize (the window size in the first step, which means the size of the neighbourhood considered
# for corner detection), ksize (aperture parameter for the sobel derivative used), k (harris detector free parameter
# in the equation)
dst = cv.cornerHarris(gray, 2, 3, 0.04)

# to get the better result we need to dilate the result image
dst = cv.dilate(dst, None)

# we are reverting back to the original image with optimal threshold value
# if our pixel value in our result from the method cornerHarris is greater than 0.01 * (max pixel value in the result matrix)
# this is the interested point of the corner
img[dst > 0.01 * dst.max()] = [0, 0, 255]


cv.imshow("dst", img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()