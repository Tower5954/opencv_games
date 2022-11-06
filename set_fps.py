<<<<<<< HEAD
import cv2
import time


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
print("FPS", cap.get(cv2.CAP_PROP_FPS))

last_time = time.time()

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    text = "FPS: " + str(int(1/(time.time() - last_time)))
    last_time = time.time()
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

=======
import cv2
import time


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
print("FPS", cap.get(cv2.CAP_PROP_FPS))

last_time = time.time()

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    text = "FPS: " + str(int(1/(time.time() - last_time)))
    last_time = time.time()
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

>>>>>>> origin/master
