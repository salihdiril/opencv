import cv2

# we can use VideoCapture method with working videos in OpenCV
# first argument is a filename of a video which we want to work
# or we can use our camera device's index. It is 0 for some computers and -1 for others
cap = cv2.VideoCapture(-1)
# print(f"cap.isOpened(): {cap.isOpened()}")

# for creating video we use video capture class
# and for saving the created video we'll use video writer class
# this class will take a few argument
# first one is a name for the video that we are going to save
# the second one is FOURCC code which is a 4 byte code which is used to specify the video codec
# now we'll take a fourcc code from video writer_fourcc class
# this class will take four byte code that is called XVID
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') # we can also write as (*"XVID")
# now we can pass fourcc object as a second argument
# third argument is number of frames per second
# fourth argument is size which is the windows height and width as a tuple format
save = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

# we want to capture frames of the video continuously, so we will use while loop
# we can also use isOpened function of cap video capture object 
# it will return false if the given video name or index is wrong
while cap.isOpened():
    
    # We will capture frames and store it with read method of cap variable which is a video capture object
    # if frame variable is available ret variable will be true and the frame data will be stored in frame
    # otherwise ret will be false
    ret, frame = cap.read()

    # we will save frames if they are available
    if ret == True:

        # we can also be informed the size of the frame
        # print(f"Height: {cap.get((cv2.CAP_PROP_FRAME_HEIGHT))}")
        # print(f"Width: {cap.get((cv2.CAP_PROP_FRAME_WIDTH))}")

        # we can save the frames as a video with save video writer object's write method
        save.write(frame)

        # we can also convert the captured colored image to grayscale image
        # first argument takes an image source which is frame variable
        # second argument takes a code. We'll give grayscale code
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # now we can show the captured frame in a window with imshow method
        cv2.imshow("frame", gray)

        # the next thing we should do is making the window wait 
        # and we will make the window quit when we press q
        # in the documentation of the cv2.waitKey method it is said that it is better if we mask the method with "0xFF"
        # if we have 64bit OS
        if cv2.waitKey(1) & 0xFF ==  ord('q'):
            break
    else:
        break

# we need to release the resource after we have done with capturing frames with our camera
cap.release()
# we also need to release save's resource
save.release()
cv2.destroyAllWindows()
