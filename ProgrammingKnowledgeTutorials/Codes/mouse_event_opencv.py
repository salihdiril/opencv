import numpy as np
import cv2

# mouse events can be double click, click, roll etc.
# now we want to hold all the mouse events in a list
# we'll use dir built-in method
# dir will show all the classes, functions, members of cv2
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(f"Events in cv2 package: {events}")

# now we'll create a function that listens mouse events
# our function will take event which is happened when we click with mouse as first parameter
# second and third parameters will be the coordinates of mouse (x, y)
def click_event(event, x, y, flags, param):
    # we'll show x, y coordinates when we click left button of mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"x: {x}, y: {y}")
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('image', img)
    
    # Now we want to listen right click event
    if event == cv2.EVENT_RBUTTONDOWN:
        # img is a matrix and we can use multiple indexing in 3D array
        # 0 is the first value of BGR
        # x and y are coordinates
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (200, 255, 122), 2, cv2.LINE_AA)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("lena.jpg", -1)
cv2.imshow('image', img)

# we'll use setMouseCallback function to call our callback function which we have created which is click_event function
# whenever somebody clicks on image which we are showing the video in a window
# first parameter will be the name of our image. The name should be the same with the cv2.imshow function's name parameter
# inside our callback function and inside the main function
# second parameter is the callback function which catches the mouse events
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

