import cv2


logo = cv2.imread("Why.A.I..png")
print(logo.shape)
logo = cv2.resize(logo, (100, 100))
logo = cv2.resize(logo, (500, 500))
cv2.imshow("logo", logo)

cv2.waitKey(0)