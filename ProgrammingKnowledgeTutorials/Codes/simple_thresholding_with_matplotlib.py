import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("gradient.png", 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 23, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 23, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    # subplot method takes a few arguments
    # first one is the number of rows which we want to show in our plot
    # second one is the column number
    # third one is the index of the image
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

