import cv2

image = cv2.imread("hello.jpeg")
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0)
cv2.imshow("copyMakeBorder", image)
cv2.waitKey(0)
cv2.destroyAllWindows()