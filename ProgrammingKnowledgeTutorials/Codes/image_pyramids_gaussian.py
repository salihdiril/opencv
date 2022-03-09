import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# till now when we deal with images we use them at constant size, but sometimes we need to use images
# with different resolutions. For example if we want to deal with faces inside images, we'll get different
# sizes of images because faces can be different size inside images. SO using image pyramids we just create the images
# of different resolutions and then we search for the object    
# Pyramid, or pyramid representation, is a type of multi-scale signal representation in which a signal or an image
# is subject to repeated smoothing and subsampling. When you blur an subsample input image the resolution will be halved
# there is two types of image pyramid: Gaussian Pyramid and Laplacian Pyramid

img = cv.imread("lena.jpg")

# first we'll talk about gaussian pyramid. Gaussian pyramid is nothing but repeated filtering and subsampling of an image
# there are 2 functions available for gaussian pyramid in opencv which is called pyrDown and pyrUp
# In order to use pyrDown function we define some variables. lr for lower resolution
# pyrDOwn parameters: source
# when we apply pyrDown transformation to the image its resolution will be one fourth of original image
""" lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)
 """
# there is also pyrUp method in gaussian pyramid which increase the resolution
# hr for higher resolution, parameters of pyrUp: source
""" hr2 = cv.pyrUp(lr2)
hr1 = cv.pyrUp(hr2) """
# hr0 = cv.pyrUp(hr1)
# if we apply pyrUp method to the image that is applied pyrDown method and has gotten reduced resolution the new image's
# size will be equal to the original image that is not applied pyrDown method. But the immages won't be the same
# because when we apply pyrDown 'method to an image we lose some information (pixels) and when we use pyrDown to the 
# reduced resoluted image we won't gain any information. We just multiply the pixels and obtain copied pixels to increase
# the resolution and that's why we obtain blurred version of the original one


# when we want to create a pyramid of multiple resolution instead of using pyrup and pyrdown methods repeatedly we just get a copy
# of the original image with copy function of image object and create a gaussian pyramid array 
# Afterwards we can use gaussian pyramid in a for loop
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv.pyrDown(layer) 
    gp.append(layer)
    cv.imshow("layer"+str(i), layer)

cv.imshow("Original Image", img)
# cv.imshow("pyrDown 1 image", lr1)
# cv.imshow("pyrDown 2 image", lr2)
# cv.imshow("pyrUp 2 image", hr2)
# cv.imshow("pyrUp 1 image", hr1)
# cv.imshow("pyrUp 0 image", hr0)

cv.waitKey(0)
cv.destroyAllWindows()