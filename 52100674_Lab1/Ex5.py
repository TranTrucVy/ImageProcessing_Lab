import cv2

image = cv2.imread("hello.jpeg")

start_point = (0, 0)
end_point = (800, 800)
color = (0, 255, 0)
image = cv2.arrowedLine(image, start_point, end_point, color, 150, tipLength = 0.5)
cv2.imshow("Line in image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()