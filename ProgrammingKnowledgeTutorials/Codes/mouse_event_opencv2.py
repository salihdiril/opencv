import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    
    # we want to draw a circle every time we click down the left button of the mouse
    # then when we click down another point in the window then we'll going to draw a line
    # between those two points
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        
        # we'll save wherever the mouse clicked; hence, we can draw a line between two clicked points
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)

img = np.zeros((512, 512, 3), np.uint8)
#img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()