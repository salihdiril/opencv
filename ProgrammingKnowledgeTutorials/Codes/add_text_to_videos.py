import cv2

cap = cv2.VideoCapture(-1) 

# we can learn many properties of cap video capture object using get function
# every propert also has its own number e.g instead of writing "cv2.CAP_PROP_FRAME_HEIGHT"
# we could write 3 (if the code of that property is 3)
print(f"Height: {cap.get((cv2.CAP_PROP_FRAME_HEIGHT))}")
print(f"Width: {cap.get((cv2.CAP_PROP_FRAME_WIDTH))}")

# we can set some properties of cap vşdeo capture object using set method
# first argument will be the property and second argument will be the value that we want to set
# if we give too big values it will be set the max resolution that our camera can give (1280,720)
cap.set(3, 12800) # 3 = cv2.CAP_PROP_FRAME_WIDTH
cap.set(4, 7200) # 4 = cv2.CAP_PROP_FRAME_HEIGHT
print(f"Height: {cap.get((4))}")
print(f"Width: {cap.get((3))}")

while cap.isOpened():

    ret, frame = cap.read()

    if ret == True:

        gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()