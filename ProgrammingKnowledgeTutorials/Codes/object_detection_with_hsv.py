import numpy as np
import cv2 as cv

# in this program we'll try to detect objects using HSV (Hue, Saturation, Value)
# Hue corresponds to the color components (base pigment), hence; just by selecting a range of
# hue, you can select any color (0-360)
# Saturation is the amount of color (depth of the pigment) (dominance of hue) (0-100%)
# Value is basically the brightness of a color (0-100%)
# RGB color space are all correlated to the color luminance that is what we loosely call intensity
# i.e (in other words), we cannot seperate color information from luminance
# HSV color space is used to seperate image luminance from color information  
# so this makes it easier when we are working on or we need luminance in our images
# we use HSV color space in the situation where color description plays a very important role
# HSV also known as hexagon color model
# According to the hexagon color model, hue is the variety of color pigments that is represented at the base of the
# hexagon. Saturation is the amount of pigment of a color which is represented by a range of different tones of the
# same color between inside of the hexagon and the outside edge of the hexagon. Value is the brigthness, transparency
# of the colors which is represented a range of colors between the corner, vertex of the hexagon and the base of the hex

def nothing(x):
    pass

cap = cv.VideoCapture(-1)

# it's not easy to detect the lower and upper value of a color
# so we'll use tracker to detect them
cv.namedWindow("Tracking")
# LH = Lower Hue --- LS = Lower Saturation --- LV = Lower Value
# UH = Upper Hue --- US = Upper Saturation --- UV = Upper Value
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:

    #  let's say we only want to detect green or blue balls inside the smarties.png image
    # frame = cv.imread('smarties.png')
    # we can also capture frames from our camera to detect only some objects
    _, frame = cap.read()

    # to detect ball according to their colors, first we need to convert our colored image to hsv image
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_hue = cv.getTrackbarPos("LH", "Tracking")
    lower_saturation = cv.getTrackbarPos("LS", "Tracking")
    lower_value = cv.getTrackbarPos("LV", "Tracking")
    upper_hue = cv.getTrackbarPos("UH", "Tracking")
    upper_saturation = cv.getTrackbarPos("US", "Tracking")
    upper_value = cv.getTrackbarPos("UV", "Tracking")

    # next step is thresholding our hsv image for a range of blue color
    # we already know the exact hsv values of the lower value
    # if we don't know the values, we need to use a tracker
    lower_blue = np.array([lower_hue, lower_saturation, lower_value]) 
    upper_blue = np.array([upper_hue, upper_saturation, upper_value])

    # now we need to threshold our hsv image to get only blue color
    # to do that we are gonna use inRange method of cv2 package
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # now we'll do bitwise operations
    res = cv.bitwise_and(frame, frame, mask=mask)


    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()