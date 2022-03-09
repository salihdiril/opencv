import cv2 as cv
import numpy as np

# In this program we'll try to track people that's moving
# we'll have rectangles around the moving people. When they are moving
# rectangles will appear arount them and when they don't move rectangle will disappear
# we'll also have status variable that tells if a person moving or stopping.

cap = cv.VideoCapture('vtest.avi')

# first we'll read two frames from the video
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    # we are going to find the difference between the first frame and the second frame
    # we'll use absdiff method to find absolute difference between the two frames
    diff = cv.absdiff(frame1, frame2)
    # we are going to find contours of the images, so we use grayscale image for our convenience
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    # now we'll blur grayscaled image with gaussian blur
    blur = cv.GaussianBlur(gray, (5,5), 0)
    # now we are going to find the threshold
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    # next step is dilate the thresholded image to fill in all the holes. This will
    # help us to fing out better contours
    dilated = cv.dilate(thresh, None, iterations=3)
    # now we are going to find contours
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # This time we'll draw the contours. We want to apply drawing on the original image. That's why
    # we use frame1 as a source.
    # with the operations inside the while loop we obtain contours and draw them 
    # because we calculate the differences between the sequential frames of the video
    # we got contours around the moving object. However we wanted to use rectangles as
    # contours and we don't want any other contours except humans, but we had contours because
    # of the moving ropes inside the video. So we take those contours as a noise and we want to remove those noises
    # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # now we are going to iterate contours with for loop
    # contours is a list and it is iterable.
    for contour in contours:
        # first step is save all the coordinates of the fount contours
        # there is a method which is called boundingRect which we are going to apply on the contour
        # this method will return x and y coorinates and width and height
        # (x-coordinate, y-coordinate, width, height)
        (x, y, w, h) = cv.boundingRect(contour)
        # the next step is finding the area of the contour and then we are going to say if this area
        # less than a certain value then we don't want to do anything otherwise we want to draww a rectangle on it
        # we use contour area method to calculate are
        if cv.contourArea(contour) < 700:
            continue

        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # next step is printing some text if a movement observed
        cv.putText(frame1, f"Status: {'Movement'}", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3) 

    cv.imshow("feed", frame1)
    # now we save frame2 inside frame1 and take the second frame and assign it to frame2
    # Consequently we can calculate the differences and other operations again in the next tour of while loop
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
cap.release()