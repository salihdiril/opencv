from datetime import datetime
import cv2
import datetime

cap = cv2.VideoCapture(-1)
cap.set(3, 1280)
cap.set(4, 720)

while cap.isOpened():

    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()