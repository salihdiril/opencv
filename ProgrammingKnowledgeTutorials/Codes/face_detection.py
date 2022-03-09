import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# in this program we are going to discuss about basics of face detection using "Haar Feature Based Cascade Classifiers"
# Object detection using haar feature based cascade classifiers is an effective object detection method proposed by 
# Paul viola and Michael Jones in a paper. Haar feature based cascade classifier is a machine learning (ML) based approach
# where a cascade function is trained with a lot of positive and negative images.
# First, a classifier (namely a cascade of boosted classifiers working with haar-like features) is trained with a few
# hundred sample views of a particular object (i.e, a face or a car), called positive examples, that are scaled to the same
# size (say, 20x20), and negative examples - arbitrary images of the same size
# so if we want to train an ML program for detecting faces, we feed it with face images and they are called positive images
# and we also provide some arbitrary images that does not contain the object that we are searching, in our case faces, which
# are called negative images.
# after a classifier is trained, it can be applied to a ROI of an input image and the classifier output will be 1 if the 
# region is likely to show the object or 0 otherwise.

# opencv comes with a trainer and a detector, so if we want to train our classifier for any object (e.g, a watc, a car etc)
# then we can use this classifier. In opencv github page we can find some trained classifier XML files.
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# we are going to detect the face, hence; we are going to use haarcascade_frontalface_default.xml trained classifier 

# we'll define our classifier
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv.imread("test_face_2.jpg")
# our classifier works with grayscale images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# object = cv.CascadeClassifier.detectMultiscale(image, scaleFactor, minNeighbours)
    # image: Matrix of the type CV_8U containing an image where objects are detected.
    # objects: Vector of rectangles where each rectangle contains the detected object, the rectangles maybe
    #         partially outside the original image
    # scaleFactor: Parameter specifying how much the image size is reduced at each image scale
    # minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# the last step is to iterate over all the faces which we have detected and draw a rectangle on them
for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=3)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()