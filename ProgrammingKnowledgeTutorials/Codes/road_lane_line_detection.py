import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# we'll make a project about findin lane lines in a road with the concepts that we have learned
# we have a road image an we want to detect the 2 continuous white lane line that's on the left and right
# side of the road and we want to detect discrete lane line that's placed middle of the road

def region_of_interest(img, vertices):

    # we create a blank image that has the same shape with given image using zeros like method
    mask = np.zeros_like(img)

    # now we save the channel number of the given image
    # we use grayscale image so we don't need depth
    # num_channel = img.shape[2]

    # next we'll match color using num_channel
    match_mask_color = 255
    # now we fill inside the polygon using fillPoly method. We want to mask every other region outside of ROI 
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    # we actually copy our image to a new variable so we won't be able to distort the original image
    img = np.copy(img)
    # now we have a black image that has size equivalent to the original image
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    # now we can loop around the lines vector that has deetected lines
    for line in lines:
        # line gives us four parameters: coordinates of the first point in the line, coordinates of the
        # second point in the line
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

    # now we are going to merge the blank image with original image using addWeighted method 
    # addWeighted method gives weight images to decide how much we take from each image when we merge them
    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

image = cv.imread("road.png")

# the next step is to define the region of interest (ROI)
# if we look at the image we'll see lanes are paralel to each other and at some point they will merge
# hence our ROI will be a triangle format
# when we draw a triangle we'll ignore some part of the left lane but that lane isn't important because
# we need to look at the right lane when we drive. We drive our car on the rigth side of the road

# first we prinnt shape, height and width of the image
print(f"shape of the image: {image.shape}")
height = image.shape[0]
width = image.shape[1]

# now let's try to define our ROI. We'll define three points which are the corners of the triangle
region_of_interest_vertices = [
    (0, height),            # left corner
    (width/2, height/2),    # middle corner (merging point of the lanes)
    (width, height)         # right corner
]
print(region_of_interest_vertices)

# now we came a point where we are able to find ROI. Next step is finding the lanes
# we are going to find edges so we need to convert our cropped image to a grayscale image
gray_roi = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# we use canny edge detector as edge finding method
canny_image = cv.Canny(gray_roi, 100, 200)

# now we are going to define a function that will mask every other region outside of ROI
masked_img = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32),)

# there is a problem with our image that applied canny edge detector method. Our edge image contains roi's limits as 
# an edge also, however it shouldn't be because roi's limits are not lane lines. hence we should remove those limits
# this can be done by first detecting the edges and then finding the ROI
# the next step is draw the lines using the edges inside the ROI with hough line transform
# houghLineP method returns line vector of all the lines which are detected inside the image we provided to the method
lines = cv.HoughLinesP(masked_img, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)
image_with_lines = draw_the_lines(image, lines)

cv.imshow("Original image", image)
cv.imshow("ROI image", masked_img)
cv.imshow("Lane lines image", image_with_lines)
cv.waitKey(0)
cv.destroyAllWindows()


