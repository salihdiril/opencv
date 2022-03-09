import cv2 as cv
import numpy as np

# in this program we are goint to learn an object tracking method called meanshift 
# object tracking is the process of locating a moving object over time using a camera
# idea behind meanshift is;
# We have a window that has rectangle or circle shape and the window's size is small. We need to shift that
# window to the area of the maximum pixel density. The algorithm steps are;
    # 1 - we pas the initial location of a target object and histogram back projected image to a meanshift function
    # 2 - As the object moves the histogram back projected image also changes
    # 3 - the meanshift function moves the window to a new location with the max probability density

cap = cv.VideoCapture("slow_trafic_small.mp4")

# let's say that we want our window to track each car coming to the camera
# the disadvantage side of the meanshift is we have to give initial location
# first step is we are going to take the first frame of our video
ret, frame = cap.read()

# after taking the first frame we are going to define the initial location of the car window
# in our case we want to track the first white car 
# we have already calculated the first white car's initial position
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

# next step is to define the ROI
roi = frame[y:y+height, x:x+width]
cv.imshow("ROI", roi)

# we said that in the first step we need to pass the initial location of the target and histogram
# back projected image to the meanshift function. Histogram back projection in simple words, we create an image
# of the same size but of a single channel as of our input image. In our case this will be our frame where each 
# pixel corresponds the probability of that pixel belonging to our object 
# now we are going to define our histogram back projection
# we already have ROI. Now we'll just convert this roi to hsv color space
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# for the histogram only hue is considered from hsv, the first channel and also to avoid the false value
# due to low light we use inRange function. SO these low light values are discarded using the inRange function
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))

# now we are going to calculate our histogram value
# parameters: source, channel (hue channel)
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])

# now we'll normalize our source
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
# finally we obtain histogram back projected image

# we'll setup the termination criteria, either 10 iterarion or move by at least 1 pt
term_crit = (cv.TermCriteria_EPS | cv.TermCriteria_COUNT, 10, 1)

while 1:
    ret, frame = cap.read()

    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Parameters: number of images, channels, hist value, ranges, scale
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # dst is our b-histogram back projected image. Next we'll apply the meanshift
        ret, track_window = cv.meanShift(dst, track_window, term_crit)

        # Once we have our track_window we can draw a rectangle arount our target car
        x, y, w, h = track_window
        final_image = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 3)

        cv.imshow("final image", final_image)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()