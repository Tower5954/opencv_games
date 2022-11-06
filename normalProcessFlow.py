import cv2
import time


cap = cv2.VideoCapture(0)

# This is preprocessing
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# The mainloop
while True:
    _, frame = cap.read()

    # This is the processing
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    # check frame
    print(frame)
    break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord("q"):
        break

