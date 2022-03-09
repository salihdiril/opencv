import cv2 as cv
import numpy as np

img1 = cv.imread("road.png")
img2 = np.zeros(img1.shape, dtype=np.uint8)

height = img1.shape[0]
width = img1.shape[1]

roi_corners = np.array([[(0, height), (width/2 , height/2), (width, height)]], dtype=np.int32)
channel_count = img1.shape[2]
ignore_mask_color = (255,)*channel_count
cv.fillPoly(img2, roi_corners, ignore_mask_color)


bitwise_and = cv.bitwise_and(img1, img2)
cv.imshow("bitwise and mask", bitwise_and)
cv.imshow("img1", img1)
cv.imshow("img2", img2)

cv.waitKey(0)
cv.destroyAllWindows()