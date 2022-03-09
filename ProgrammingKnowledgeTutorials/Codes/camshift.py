import cv2 as cv
import numpy as np

# in meanshift method window size that tracking the object always remain the same, however; we want windows size
# to change its size according to the target's situation. To achieve this purpose we'll use camshift method instead
# of meanshift method
# camshift stands for continuously adaptive meanshift. SO camshift algorithm applies meanshift first and once the meanshift
# converges, it updates the size of the window. In addition it also calculates the orientation of the best fitting eclipse
# to it. 
# all the codes from the meanshift program will remain the same apart from the meanshift function. We'll change it
# to the camshift algorithm.

cap = cv.VideoCapture('slow_trafic_small.mp4')

ret, frame = cap.read()
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

roi = frame[y:y+height, x:x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term_crit = (cv.TermCriteria_EPS | cv.TermCriteria_COUNT, 10, 1)

while True:

    ret, frame = cap.read()

    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # camshift algorithm return to ret value x, y, w, h and rotation values
        # so we can use rotation to rotate window
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        #x, y, w, h = track_window
        #final_image = cv.rectangle(frame, (x,y), (x+w, y+h), 255, 3)

        # we can use different approach with ret values' rotation value
        pts = cv.boxPoints(ret)
        # pts returns float so we need to convert it to integer to use in rectangle function
        pts = np.int0(pts)
        # we won't use normal rectangle method. We'll use rotating rectangle method
        # when we assign True to third parameter rectangle will be closed
        final_image = cv.polylines(frame, [pts], True, (0, 255, 0), 3)

        cv.imshow("final_image", final_image)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
