import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("lena.jpg")

# laplacian pyramids are formed from the gaussian pyramids. There is no exclusive function for creating the laplacian pyramid
# a level of laplacian pyramid is formed by the difference between that level in Gaussian pyramid and expanded version
# of its upper level in gaussian pyramid
# top level of gaussian pyramid is the last image that is applied pyrDown method
layer = img.copy()
gp = [layer]
for i in range(3):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow(str(i+1) + ". layer", layer)

# top level is the last appended image in the gp array
upper_layer = gp[3]
cv.imshow("Upper level gaussian pyramid", upper_layer)

# now let's create a laplacian pyramid array
lp = [upper_layer]
for i in range(3, 0, -1): # start from five and stop at 0 with -1 steps
    gaussian_expanded = cv.pyrUp(gp[i]) # expanded version of its upper level in gaussian pyramid
    laplacian = cv.subtract(gp[i-1], gaussian_expanded) # difference between that level and expanded version
    cv.imshow(str(i), laplacian)

# laplacian pyramid shows the edges of the images
# the laplacian and the gaussian pyramids helps us to blend the images and reconstruction of the images

cv.imshow("Original Image", img)
cv.waitKey(0)
cv.destroyAllWindows()