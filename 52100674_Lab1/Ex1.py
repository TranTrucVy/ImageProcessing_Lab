import cv2
import numpy as numpy

img = cv2.imread("hello.jpeg")
print(img)

cv2.imshow("Hello",img)
cv2.waitKey(0)
cv2.destroyAllWindows()