import cv2
image = cv2.imread("hello.jpeg")
  
font = cv2.FONT_HERSHEY_SIMPLEX
org = (100, 100)
fontScale = 1 
color = (0, 0, 0)
thickness = 5
image = cv2.putText(image, 'Tran Thi Ven', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("Text in image", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()