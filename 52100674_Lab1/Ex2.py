import cv2
import numpy as numpy
import os
img = cv2.imread("hello.jpeg")

cv2.imwrite("savedImage.jpg", img)
img1 = cv2.imread("savedImage.jpg")
cv2.imshow("savedImage",img)
cv2.waitKey(0)
cv2.destroyAllWindows()