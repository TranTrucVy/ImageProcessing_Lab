import cv2

image = cv2.imread("hello.jpeg")

start_point = (0, 0)
end_point = (1100, 1200)
color = (0, 255, 0)
image = cv2.line(image, start_point, end_point, color, 10)
cv2.imshow("Line in image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
