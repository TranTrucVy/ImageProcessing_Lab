import cv2

image = cv2.imread("hello.jpeg")
start_point = (300, 300)
end_point = (600, 600)
color = (255, 0, 0)
thickness = 2
image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
# Displaying the image 
cv2.imshow("Rectangle", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()