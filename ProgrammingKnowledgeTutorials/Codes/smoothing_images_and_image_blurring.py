import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# smoothing is also known as blurring is one of the most commonly used operation in image processing
# the most common smoothing operation is remove noise operation
# when smoothing or blurring images we can use diverse linear filters because linear filters are easy
# to achieve and also relatively fast. There are various types of filters: homogeneous filter, Gaussian filter
# Median filter, Bilateral filter ... etc.
# firstly we'll see homogeneous filter. Homogeneous filter is the most simple filter, each output pixel is the 
# mean of its kernel neighbours. In homogeneous filter each pixel contributes equal weights and that's why it's
# called homogeneous filter 
# In image processing, a kernel, convolution matrix, or mask is a small matrix. It is used for blurring
# sharpening, embossing, edge detection, and more.
# kernel matrix formed by ones and its coefficient is 1/(height aka row nums) * (width aka column nums)
# As in one dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass
# filters (HPF) etc. LPF is used to remove noise or blurring the image etc. HPF filters helps in finding edges
# in the images 

img = cv.imread("lena.jpg")
# cv displays images as BGR format. In comparison, matplotlig displays images as RGB format
# Hence we need to convert BGR to RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# now we'll create a kernel to do some operations
kernel = np.ones((5,5), np.float32)/25
# now we use homogeneous filter with filter2D method
# first argument is img, second is desired depth of the destination image (for now we give -1)
# third one is the kernel
dest = cv.filter2D(img, -1, kernel)

# when we want to achieve image blurring we need to convolve images with low-pass filters
# Parameters of blur method: source, kernel size 
# blur method is also called as averaging
blur = cv.blur(img, (5,5))

# the next filtering algorithm is gaussian filter
# gaussian filter is nothing but using different-weight-kernel, in both x and y direction
# in gaussian filter, pixels located in the middle of the kernel have the higher weight, and the weight
# decreases with the distance from the neighborhood center. SO pixels located on the side have smaller weight and
# pixels located in the middle have the higher weights
# Parameters of GaussianBlur(): source, kernel size, sigma x value (for now we'll gve 0)
# Gaussian filter designed to remove high frequency noise
gaussian_blur = cv.GaussianBlur(img, (5,5), 0) 

# Median filter is something that replace each pixel's value with the median of its neighboring pixels
# This method is great when dealing with "salt and pepper noise"
# in images there can be sudden impulses that create some white and black dots in some pixels as salt and pepper noise.
# Median blur parameters: source image, kernel size (odd numbers except 1)
median = cv.medianBlur(img, 3)

# the last filter is bilateral filter. With meddian filter we not only blur the images but also smooth the edges
# SOmetimes we need to preserve the edges. The edges sometimes can be needed to remain sharper even we smooth the image
# Parameters: source, diameter of each pixel neighborhood that is used during the filter, sigma color and sigma space 
bilateral = cv.bilateralFilter(img, 9, 75, 75)

titles = ["image", "2D Convolution", "blur", "Gaussian Blur", "median", "bilateral"]
images = [img, dest, blur, gaussian_blur, median, bilateral]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()