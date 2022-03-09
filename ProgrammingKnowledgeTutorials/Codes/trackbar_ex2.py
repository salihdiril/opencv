import numpy as np
import cv2 as cv

# in this program we want to create trackbars for writing some values on the image

def display_number_on_image(x):
    print(x)


cv.namedWindow("image")
cv.createTrackbar('Current Pos', "image", 30, 3000, display_number_on_image)

switch = "color/gray"
cv.createTrackbar(switch, "image", 0, 1, display_number_on_image)

while True:
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('Current Pos', "image")
    font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4, (15, 200, 25), 10)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    switch_value = cv.getTrackbarPos(switch, "image")
    if switch_value == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image', img)

cv.destroyAllWindows()

