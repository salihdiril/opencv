import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# template matching is a method of searcing and finding the location of a template image inside a larger image
# in opencv, there is a method called match template for achieving this purpose.

img = cv.imread("messi5.jpg")
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# we grab messi's face inside messi5.jpg image and save it as messi-face.png.
# Our goal is match the messi's face template which is messi-face.png in the messi5.jpg image
# first we sholud load our template as a grayscale image
template = cv.imread("messi-face.png", 0)

# now we'll use our match template function and save the result in a variable
# parameters: source, template (which we will try to find inside a larger image), method (there are several methods
# available for the template matching. For now we are going to use TM_CCOEFF_NORMED)
res = cv.matchTemplate(grey_img, template, cv.TM_CCOEFF_NORMED)
# res variable will return an array of arrays. There will be small values. We are looking for the brightest pixel 
# That pixel is the top-left corner of the template. SO how can we filter out that brightest point inside the matrix?
print(f"res: {res}")

# now we are going to try to find the brightest point with numpy method where which is used to find values which is greater
# than certain values. Now, we are gonna define a threshold value that filters out the brightest point
# if there are several points that's greater than threshold we can increase the threshold until only one
# point is returned 
threshold = 0.95

# next, we are going to use where method
# parameters: source (matrix) >= threshold (this will return us all the values greater than threshold value inside
# the matrix). 
loc = np.where(res >= threshold)
print(f"values greater than threshold: {loc}")

# After we find the brightest point we can draw a rectangle around those points that's size is equal to the template
# and find the template inside the larger image
# first we should save our template's width and height. [::-1] means we want to get the column and row number in reverse
# order
width, height = template.shape[::-1]
print(f"width: {width} and height: {height}")

# if we had multiple template that's taken from larger image we should filter out the template we are looking for
# when threshold value a little lower, there will be multiple points and the loop below will iterate multiple times
# as a result rectangle will be much thicker
for pt in zip(*loc[::-1]):
    # first point will be top-left and second will be bottom right. To find bottom right we shoul add template
    # size to the point
    cv.rectangle(img, pt, (pt[0] + width, pt[1] + height), (0, 0, 255), 2)


cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()