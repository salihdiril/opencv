import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# now we are going to find the road lanes within a video
# we are going to use video frames instead of a road image

def find_roi(img, vertices):

    mask = np.zeros_like(img)
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

def draw_lanes(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=5)
    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

# we are going to define a process method which takes video frames and find the lane lines
def process(image):

    height = image.shape[0]
    width = image.shape[1]

    roi_vertices = [(0, height), (650, 531), (1073, 700)]
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    canny_image = cv.Canny(gray_image, 100, 200)
    roi_image = find_roi(canny_image, np.array([roi_vertices], dtype=np.int32), )
    lines = cv.HoughLinesP(roi_image, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=20, maxLineGap=100)
    lanes_image = draw_lanes(image, lines)
    return lanes_image

cap = cv.VideoCapture("Lane Detection Test Video 01.mp4")

while cap.isOpened():

    ret, frame = cap.read()
    frame = process(frame)
    cv.imshow("frame", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()