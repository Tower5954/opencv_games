import cv2

cap = cv2.VideoCapture(0)

width = cv2.CAP_PROP_FRAME_WIDTH(cap, 640)
height = cv2.CAP_PROP_FRAME_HEIGHT(cap, 480)

in range