import cv2

image = cv2.imread("hello.jpeg")
center_coordinates = (120, 100)
radius = 30
color = (0, 0, 255)
thickness = -1
thickness1 = 5
# image = cv2.circle(image, center_coordinates, radius, color, thickness)

image = cv2.circle(image, center_coordinates, radius, color, thickness1)

cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.imshow("Circle", image1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()