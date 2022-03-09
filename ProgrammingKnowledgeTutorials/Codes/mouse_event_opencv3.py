
import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    # we want to show the BGR values of the clicked point in the image window on another window
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (200, 100, 255), -1)

        # we create a black image and we want to fill this image with the BGR values of the clicked point
        my_color_img = np.zeros((512, 512, 3), np.uint8)

        # this notation means we want to assign the value of the right side of the statement to every channel
        # every point in the image
        my_color_img[:] = [blue, green, red]
        cv2.imshow('color window', my_color_img)



img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()