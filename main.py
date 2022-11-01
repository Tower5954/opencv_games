# install opencv-python version: 4.5.5
import cv2
import time

print(cv2.__version__)

cap = cv2.VideoCapture(0)

# find out how fast the webcam is. 30fps is the goal
last_time = time.time()
while True:
    _, frame = cap.read(0)

    # resize the frame
    frame = cv2.resize(frame, (640, 480))

    text = "FPS: " + str(int(1/(time.time() - last_time)))
    last_time = time.time()

    cv2.putText(frame, text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 125, 0), 2)
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

