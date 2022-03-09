import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# we'll discuss different morphological operations such as erosion, dilation, opening and closing methods ... etc
# Morphological transformations are some simple operations based on image shape, normally performed on a binary image
# there are 2 things which are required when we deal with morphological operations: First is the original image
# and second is called a structuring element or a kernel which decides the nature of the operation

img = cv.imread("smarties.png", cv.IMREAD_GRAYSCALE) # we can also write 0 for IMREAD_GRAYSCALE

# normally we do morphological operation on binary images. So we use threshold method
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

# when we look at the masked image we could see black dots inside the white balls
# let's try to remove those dots
# we are going to use dilation transformation with dilate method
# this method takes two arguments
# first one is a source which is an image
# second one is a kernel which is a square or some shape which we want to apply on the image
# with dilation we reduce the size of the black dots in the mask image
# so how do we remove those dots completely?
# There is a third parameter that we can give to the dilate method, which is iteration
# if we use bigger kernel then the balls will start merging because when we apply kernel then 
# if there is one pixel which is one under the kernel then that pixel will be one. That's why
# white ball's are become bigger
kernel = np.ones((2,2), np.uint8)
dilation = cv.dilate(mask, kernel, iterations=2)

# We can't keep using dilation with bigger kernels or bigger iterations. This is where
# we'll use erosion morphological operation
# first argument will be source, second will be kernel, and third argument is an optinal argument
# which is iteration
# with erosion sides of the white balls are eroded and their sizes have gotten smaller
# kernel will wander around the image and a pixel will be one only when the all the pixels under the 
# kernel will be 1, otherwise the pixel will be set as 0
erosion = cv.erode(mask, kernel, iterations=1)

# there are two more morphological operations which are opening and closing
# we use morpologyEx method and it takes a few parameters
# first one is source, second is the type of morphological operation which we want to perform
# third one is kernel
# opening is just another form of erosion followed by dilation so when you performe opening
# first of all erosion will be performed on the source image and dilation will be performed on the source.
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

# there is also closing operation which is the opposite of the opening operation
# dilation is performed first, and after that erosion will be performed
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

titles = ["images", "mask", "dilation", "erosion", "opening", "closing"]
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show() 
