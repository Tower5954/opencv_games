import cv2

logo = cv2.imread("Why.A.I..png")

logo = cv2.resize(logo, (100, 100))

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
print(gray)

_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
print(mask)