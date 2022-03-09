import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# an image gradient is a directional change in the intensity or color in an image
# image gradient of an image is one of the fundamental building block of image processing
# we use image gradient for finding edges inside an image
# there are several image gradient methods available in opencv
# we are going to see 3 of them in this program
# first is laplacian derivative, secon is sobel x method and third is sobel y method
# all this methods which I pointed above are different gradient functions which uses different mathematical operations
# to produce the required image. Laplacien calculates laplacien derivatives, sobel method joint Gaussian and differentiation
# operations. These functions are just the tools which we find the gradient of images and analyse the image

img = cv.imread("sudoku.png", cv.IMREAD_GRAYSCALE)

# now let's see how we apply laplacian gradient on an image
# Parameters: source, datatype which we are going to use (cv.CV_64F, 64 bit float due to negative slope
# induced by transformin image from white to black), kernel size (must be odd)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
# now we are gonna take absolute value of our laplacien image transformation and we are going to convert
# its value back to the unsigned 8-bit integer which is suitable for our output
lap = np.uint8(np.absolute(lap))

# now let's apply sobel x and sobel y gradient methods which is also known as sobel gradient representation
# Sobel method parameters: source, datatype, dx which specifies whether we'll use sobelX or sobelY method (this value
# can take 1 or 0. 1 for sobelX, which is for x direction), dy which is for y direction 
# dx stands for order of derivatives x and dy stands for order of derivative y
# we can also provide kernel size if we want to as a fifth parameter
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
# Again we are gonna convert sobelX and sobelY values to unsigned int datatype
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
# When we apply sobelX gradient method, the change in direction in the intensity is in the x direction 
# with sobelY the change in direction in the intensity is in the y direction

# we can also combine sobelX and sobelY images
sobel_combined = cv.bitwise_or(sobelX, sobelY)

titles = ["image", "Laplacien Gradient Image", "SobelX", "SobelY", "Combination of SobelX and SobelY"]
images = [img, lap, sobelX, sobelY, sobel_combined]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()