import numpy as np
import cv2

# bitwise operations could be very useful when we use masks
# masks are binary images that indicates the pixel in which an operation is to be performed
# we create an image that's shape and size are equal to image_1.png
# we'll use these below images for bitwise operations
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('image_1.png')

# Firstly we'll do bitwise and operation with cv2.bitwise_and method
# this method takes several arguments
# source of first image, source of second image, destination which is None by default, and mask which is
# also optinal as destination parameter
# bitwise and work bit by bit and operation. only 1 and 1 will return 1 in and operation.
bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_not = cv2.bitwise_not(img2)
bit_xor = cv2.bitwise_xor(img2, img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_xor", bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
