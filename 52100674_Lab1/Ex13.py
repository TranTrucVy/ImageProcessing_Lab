import cv2

image = cv2.imread("hello.jpeg")
cv2.imshow('Original', image)
cv2.waitKey(0)
# Using HSV color space. HSV color space is mostly used for object tracking.
img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )
cv2.imshow("Image convert", img)
cv2.waitKey(0)
cv2.destroyAllWindows()