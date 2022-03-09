import cv2 as cv
import numpy as np

# in this program we will learn backgroun subtraction method. First of all what is background subtraction?
# background subtraction is common and widely used technique for generating the foreground mask which is
# also known as binary image containing the pixels belonging to the moving object of a scene when
# these images are captured using static camera and as the name suggests background subtraction calculates
# foreground mask performing the subtraction between the current frame and the background model containing the
# static part of the scene. We can use background subtraction to detect visitors who are leaving or enterind the room
# there are several algorithms which were introduced for the purpose of this background subtraction and opencv implemented a
# few of them

cap = cv.VideoCapture("vtest.avi")

# fgbg: foreground-background
# below bg(background) subtraction method is a gaussian mixture based bg and fg(foreground) segmentation algorithm
# so using "bgsegm" word what we are doing is that we are just creating bg object of the function using
# createBackgroundSubtractorMOG() method. This method takes a few parameters
# Parameters: history, number of gaussian mixtures and threshold. All of them are set by default
# there is also another createBackgroundSubtractorMOG2() method which is directly available in opencv
# in this method there is detectShadows parameter which is set True by defauld. Shadows displayed in gray color
# if we set it as false then shadows also displayed in white
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)

# there is another bg subtr. method called createBackgroundSubtractorKNN. It takes optional parameters
# which is set by default, so we don't need to set any of them
fgbg2 = cv.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()

    if frame is None:
        break

    fgmask = fgbg2.apply(frame)

    cv.imshow("Frame", frame)
    cv.imshow("Fgmask frame", fgmask)

    keyboard = cv.waitKey(30)

    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()