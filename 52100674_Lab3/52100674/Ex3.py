import cv2 
import numpy as np
# Read image 
src = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE); 
# Basic threhold example 
th, dst = cv2.threshold(src,179,255, cv2.THRESH_BINARY_INV); 
cv2.imwrite("opencv-threshold-example.jpg", dst); 
dst_2=src.copy()
for x in np.arange(0,len(dst_2)):
    for y in np.arange(0,len(dst_2[0])):
        if(dst_2[x][y]>190):
            dst_2[x][y]=0
cv2.imwrite("opencv-threshold-example_1.jpg", dst_2); 
 
 
image = cv2.imread('input_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)

mask = cv2.bitwise_not(binary_image)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_contour_area = 100
filtered_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area >= min_contour_area:
        filtered_contours.append(contour)
img_cut=[]
for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    img_cut.append(image[y:y+h,x:x+w])
for i in np.arange(0,len(img_cut)-1):
    cv2.imshow('Bong'+str(i),img_cut[i])
    cv2.waitKey(0)