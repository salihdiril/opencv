import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# We alread learned how to detect corners using cornerHarris method. In this program we'll learn how to detect
# corners using Shi Tomasi corner detection method. Shi tomasi method is similar to harris corner detection but 
# calculating the R score is a bit different. Shi tomasi method gives us better result in comparison to harris corner
# detector and also with shi tomasi corner detector we can find the top end corners which means we can provide 
# the number of corners we want and this might be useful in case where we don't want to detect all the corners inside
# an image

img = cv.imread("pic1.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Shi and tomasi explain their methods in the article called good features to track and that's why opencv
# named the method using shi tomasi corner detector as "goodFeatureToTreack". 
# Parameters: Source (grayscaled imaeg), max number of corners (if there are more than 25 corners in the image 
# then this method returns only the strongest corners), quality level (this parameter characterizing the minimal
# expected quality of the image corner), min distance (the minimum possible euclidian distance between the returned
# corners) 
corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)

# once we detected corners we convert those values into the integer values. Int0 is a mere alias for int64
corners = np.int0(corners)

# now we are going to find x and y values which is the coordinates of the found corners
for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, 255, -1)

cv.imshow("dst", img)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()