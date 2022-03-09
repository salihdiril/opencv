import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

# img.shape property returns a tuple of number of rows, columns, and channels
print(f"img.shape: {img.shape}")

# img.size property returns the total number of pixels that is accessed
print(f"img.size: {img.size}")

# img.dtype returns the image datatype that is obtained
print(f"img.dtype: {img.dtype}")

# cv2.split() method will split the channel into BGR values
b, g, r = cv2.split(img)

# if we have BGR channels sperately and want to merge them to creatge a new image we could use 
# cv2.merge method
img = cv2.merge((b, g, r))

# ROI is stands for Region Of Interest
# Sometimes we need to work certain part of image e.g. in messi5.jpg image we could have wanted to work only with the ball
# or the face of the Messi. So these certain parts of the image are called ROI of the image
# Now we want to copy the ball and paste it in another place of the image
# we've already learned how to obtain coordinates of the clicked button 
# all the pixels between 280-340 x coordinates and 330-390 y coordinates with all three BGR channels is copied into ball
ball = img[280:340, 330:390] 
# we'll place the ball image into another place of the image with below statement
img[273:333, 100:160] = ball

# now we want to add two images
# this method calculates the per-element sum of two arrays or an array and a scalar
# first and second arguments are the sources which is img and img2
# there are other parameters but we don't set them for now.
# we'll get an error if the sizes of the images do not match
# we can resize the images to match them
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
dst = cv2.add(img, img2)


# there is also addWeighted method. If we want to take %80 of from one source and %20 from the other source
# we can use this addWeighted method
# first argument is first source, second is weight of the first source that we want to take
# third is second source, and fourth is the weight of the second source
# fifth value is bias
dst2 = cv2.addWeighted(img, .8, img2, .2, 0)

cv2.imshow('image', dst)
cv2.imshow('image2', dst2)
cv2.waitKey(0)  
cv2.destroyAllWindows()

