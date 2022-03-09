import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
# our ROI for eye detection is face because eyes can only be inside a face
eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
img = cv.imread("test_face_2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for x, y, w, h in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

    # we will define our ROI which is the face inside the input image
    roi_gray = gray[y: y+h, x: x+w]
    roi_color = img[y: y+h, x: x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    # after detecting eyes, we need to iterate over those eyes and draw a ractangle upon them

    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 5)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
