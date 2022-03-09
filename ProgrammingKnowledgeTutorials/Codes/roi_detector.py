import cv2 as cv
import numpy as np


image = cv.imread("road.png", -1)
# we create a black image that has the same shape with our road image
mask = np.zeros(image.shape, dtype=np.uint8)

height = image.shape[0]
width = image.shape[1]

# we define our roi corners (3 corner creates a triangle)
roi_corners = np.array([[(0, height), (width/2 , height/2), (width, height)]], dtype=np.int32)

# we define the depth of the image
channel_count = image.shape[2]
# we fill the roi with white color
ignore_mask_color = (255,)*channel_count
# we make a new mask that has a white triangle between roi_corners
cv.fillPoly(mask, roi_corners, ignore_mask_color)

# we mask our image. Except the roi, every other pixel will become black
masked_image = cv.bitwise_and(image, mask)
cv.imwrite("image_masked.png", masked_image)