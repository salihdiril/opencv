import numpy as np
import cv2 as cv

# trackbar is useful when we try to change some values in our image dynamically at one time

# parameter x is the current position of our trackbar ( 0-255)
# Whenever this callback function is called it will print the current position of the trackbar 
def nothing(x):
    print(x)

img = np.zeros((300, 512, 3), np.uint8)

# we create a window named image
cv.namedWindow('image')

# we use create trackbar method for creating a trackbar
# first parameter is trackbar name. We should give a name to our created trackbar because
# we can create multiple trackbars for a window. We'll give "B" as a name to our trackbar because
# we'll change blue channel's value of our image
# second parameter is the name of the window in which we use our trackbar
# This is why we create a window, to give that window as a parameter to our created trackbar
# third parameter is the initial value that we want to set of our tracker.
# fourth parameter is the final value that our tracker can be set 
# fifth parameter is a callback function that we call whenever our tracker's value changed
cv.createTrackbar('B', 'image', 0, 255, nothing)

# second trackbar will change the green channel
cv.createTrackbar('G', 'image', 0, 255, nothing)

# third trackbar will change the red channel
cv.createTrackbar('R', 'image', 0, 255, nothing)

# we can also create fourth trackbar to control changes on BGR values
# for example, if fourt trackbar's value is 0 then there will be no change on image
# otherwise, if the value is 1 then the changes is applied to the image
switch = '0: OFF\n 1: ON'
print(type(switch))
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:

    # we show our image inside our created window named "image"
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27: # ESC key
        break

    # in order to obtain our trackbars' current values we can use get method
    # first parameter is trackbar name and second is window name
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    switch_value = cv.getTrackbarPos(switch, 'image')

    if switch_value == 0:
        img[:] = 0
    else:
        # now we want to set above b, g, r values in our image
        img[:] = [b, g, r]

cv.destroyAllWindows()