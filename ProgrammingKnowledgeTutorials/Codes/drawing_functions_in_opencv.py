import cv2
import numpy as np


# img = cv2.imread("lena.jpg", 1)
# we can also create an image with numpy
# we'll create an image with numpy zeros method.
# First argument is a list that contains height, width, and depth=3
# second argument is a datatype
# the image will be black because all the pixels of the image will be zero (BRG)
img = np.zeros([512, 512, 3], np.uint8)

# we'll draw a line on the lena.jpg image.
# we'll use cv2.line method. This method takes a few arguments
# first argument is the image itself
# second and third arguments are starting and ending coordinates of the line
# fourth argument is the color of the line. It must be BGR format as a tuple
# fifth argument is the thickness of the line
# if we want to choose any color we should search "rgb color picker" and choose any color
# but we need to pay attention to the order of the colors. We need to give parameter as BGR format which is
# reverse of the RGB format
img = cv2.line(img, (0,0), (255,255), (200, 219, 24), 15)

# there is also arrowedLine function. It takes the same parameters with line function but
# this time an arrow shaped line will be drawn
img = cv2.arrowedLine(img, (0,255), (255,255), (200, 219, 24), 15)

# we can also draw a rectangle with rectangle method
# second argument is the top-left vertex coordinates
# third argument is the bottom-right vertex coordinates
# if we gave -1 as a thickness parameter rectangle's inside will be filled with given color parameter
img = cv2.rectangle(img, (300,300), (450,450), (150, 240, 120), -1)

# we can also draw a circle
# first argument will be the image itseld
# second argument will be the center of the circle
# third argument will be the radius (r) of the circle (diameter = 2r)
# fourth and fifth arguments are color and thickness
# thickness also add some pixel to the circle. For example we wanted to draw a circle with 80
# pixel size of radius and it supposed to touch the left corner of the window but the circle line cross the 
# window line. The reason of this event is thickness. Thickness adds half of its size to the inside and outside
# of the circle line. Therefore, if we want to make the circle just touch to the left window line we need to subtract
# the half of the thickness size from the radius. In the below statement we subtract 6 from 80 to prevent the circle
# exceed from the window
img = cv2.circle(img, (80, 400), 74, (60, 23, 155), 12)

# we can also put some text on the image with putText method
# first argument is the image itself and second argument is the text that we want to overwrite
# third argument is the starting point of our overwritten text
# fourth argument is fontFace argument. We need to create a font variable
font = cv2.FONT_HERSHEY_COMPLEX
# fifth argument will be the font size
# sixth argument is the color of the text
# seventh argument is the thickness of the text
# eight argument is the line type of the text
img = cv2.putText(img, "OPENCV", (100, 200), font, 3, (200, 60, 100), 5, cv2.LINE_AA)

cv2.imshow("image_lena", img)

cv2.waitKey(0)
cv2.destroyAllWindows()