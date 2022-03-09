import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# one of the applications of image pyramids is blending images
# now we want to blend or merge apple and orange images
# we'll blend left hand side of the apple image with the right hand side of the orange image

apple = cv.imread("apple.jpg")
orange = cv.imread("orange.jpg")
print(f"Apple image shape: {apple.shape}")
print(f"Orange image shape: {orange.shape}")

# let's first try to cut half of the images and then try to combine them
# there is a method in numpy called hstack. We can use it to take half of an image
# hstack takes tuples as parameter. Tuple's values are row, column and depth of the image
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
# however with this method there will be a clear line that seperates orange and apple images
# in image blending we need to blend that line also
# we need to use image pyramid techniques to blend the images. ALgorithm is:
    #1-Load the two images of apple and orange
    #2-Find the gaussian pyramids for apple and orange 
    #3-From gaussian pyramids find their Laplacian pyramids
    #4-Now join the left half of apple and right half of orange in each level of Laplacian pyramids
    #5-Finally from this joint image pyramids, reconstruct the original image

# first step is already done at the beginnig of the program by using imread method
# Second step: Find the gaussian pyramids
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Third step is generating Laplacian pyramids from gaussian pyramids
apple_copy = gp_apple[6]
lp_apple = [apple_copy]

for i in range(6, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

orange_copy = gp_orange[6]
lp_orange = [orange_copy]

for i in range(6, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

# fourth step is join the half of these images in each level
apple_orange_pyramid = []
n = 0
# zip buikt-in function used when there is two iterable object 
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# fifth and the last step is reconstructing the image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 7):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv.imshow("Apple", apple)
cv.imshow("Orange", orange)
cv.imshow("Combined image", apple_orange)
cv.imshow("Apple Orange Reconstructed Image", apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()