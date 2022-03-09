import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# In this program we'll talk about histograms in opencv
# we can consider a histogram as a graph or a plot which gives us an overall idea about the intensity
# distribution of an image.

img = cv.imread("lena.jpg", 0)
# img = np.zeros((200, 200), np.uint8)
# let's add some white pixels
# cv.rectangle(img, (0, 100), (200,200), (255), -1)
# cv.rectangle(img, (0, 50), (100,100), (127), -1)

# We can also get blue, green and red channels with split method
""" b, g, r = cv.split(img) """

"""cv.imshow("image", img)
cv.imshow("b-image", b)
cv.imshow("g-image", g)
cv.imshow("r-image", r) """

# let's calculate the histogram of the image above
# we are going to use matplotlib library's pyplot module to find histogram of an image
# we'll use plt.hist method to calculate histogram
# Parameters: source (image) [we are going to use ravel function to flatten an image and takes image matrix values into
# a 1D array], max number of pixel values, range 
""" plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256]) """
# below statement will show us a figure which represents the frequency of pixels in the image
# the histogram will tell us how many pixels the image that we want to calculate its histogram has for each
# pixel value between 0 to 256.


# we can also calculate histogram with opencv using cv.calcHist
# Parameters: source (we give input image inside square brackets as an argument), channels (if we use grayscaled
# image we can just give 0 as an index channel), image mask to find the histogram of full image (we'll give None
# because our image given in grayscale mode), hist size which represent the bin counts (this also will be given inside
# of a square bracket), range
hist = cv.calcHist([img], [0], None, [256], [0, 255])
plt.plot(hist)
plt.show()

# Histogram's uses: It can tell you whether your image has been properly exposed or not. When we take digital
# image this property will be very useful. It can also tell you whether the ligthing conditions were flat or harsh
# when you took that image. Using the histogram we can also make adjustements which will work best for our digital image

cv.waitKey(0)
cv.destroyAllWindows()