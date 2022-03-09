# matplotlib is a library that gives us to create lots of different plot
# matplotlib is a python 2D plotting library which produces publication quality figures in a variety of
# hardcopy formats and interactive environments accross platforms
# for simple plotting the "pyplot" module provides a MATLAB-like interface
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg", -1)
cv.imshow("image1", img)
# we can also display our image with pyplot module
# cv2.imshow waits for watikey method and plt.show method blocks the code so the two method don't display
# images at the same time
# also plt.show display images as RBG format and cv2.imshow display as BGR format. SO the two images
# display different colored image.
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)

# we can hide the x and y axis' lines, ticks 
plt.xticks([])
plt.yticks([])

# we need to use show method also
plt.show()

# displaying images with matplotlib has some advantages 
# first of all plt.show method shows coordinates when we travel on the image with mouse
# secondly you can save the image with matplotlib window
# thirdly we can zoom the image
# we can also configure the position of the image inside the window

cv.waitKey(0)
cv.destroyAllWindows()
