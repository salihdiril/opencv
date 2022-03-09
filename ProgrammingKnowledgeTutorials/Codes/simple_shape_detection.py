import cv2 as cv
import numpy as np

# In this program we are going to learn how to detect simple shapes
# we want to detect which shape the geometrical shapes belong to using opencv and want to
# write the shape's name on top of the geometrical shapes

img = cv.imread("shapes.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(img_gray, 40, 150, cv.THRESH_BINARY)
# now we are going to find contours
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# next step is we're goint to iterate all the contours
for contour in contours:
    # we're going to use a method called cv.approxPolyDP
    # this method approximates a polygonal curves with a specific precision
    # Parameters: Curve which is contour, epsilon which is a parameter specifying the approximation accuracy (we are
    # going to multiply 0.01 with cv.arcLength() method. This method calculates a contours parameter or a curve length
    # this method takes contour and closed parameter. Closed takes true or false values. We know that all the shapes
    # have a limited area, so it is closed)
    # third parameter of approxPolyDP is closed or open shape value
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    # now we are going to draw all the contours
    # other notation of giving the number of contours is [approx]
    # because we iterate all the contours one at a time, contour index will be 0
    cv.drawContours(img, [approx], 0, (255, 255, 255), 3)
    # next step is printing the shape
    # first of all we need to find the coordinates which we want to put our shape name on it
    # we'll use ravel method of our approx object
    x = approx.ravel()[0] + 5
    y = approx.ravel()[1] - 5
    if len(approx) == 3: # we can say it is triangle because triangle mades with 3 points
        # len(approx) will find the number of curves actually
        cv.putText(img, "Triangle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    elif len(approx) == 4:
        # if contour has 4 curve than it can be either rectangle or square
        # we try to differentiate them with boundingRect method
        x, y, w, h = cv.boundingRect(approx)
        aspect_ratio = float(w)/h
        # print(f"Aspect ratio: {aspect_ratio}")
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05: 
            # actually if it is a square aspect ration shoul be 1 however we consider the noises
            cv.putText(img, "Square", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
        else:
            cv.putText(img, "Rectangle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    elif len(approx) == 6:
        cv.putText(img, "Hexagon", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    else:
        cv.putText(img, "Circle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))


cv.imshow('shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()