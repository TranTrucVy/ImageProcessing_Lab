import cv2

image = cv2.imread("hello.jpeg")

center_coordinates = (500, 500)
axesLength = (200, 100)
angle = 0
startAngle = 0
endAngle = 360
color = (0, 0, 255)
thickness = 5
image = cv2.ellipse(image, center_coordinates, axesLength, angle,
						startAngle, endAngle, color, thickness)
cv2.imshow("Ellipse", image)
cv2.waitKey(0)
cv2.destroyAllWindows()