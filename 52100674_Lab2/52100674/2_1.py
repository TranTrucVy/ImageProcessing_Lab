import cv2
import numpy as np
import webcolors

image = cv2.imread('bong.png')


# Python program to explain splitting of channels

# Importing cv2
import cv2

# Reading the image using imread() function
image = cv2.imread('bong.png')

# Displaying the original BGR image
cv2.imshow('Original_Image', image)

# Using cv2.split() to split channels of coloured image
b,g,r = cv2.split(image)

# Displaying Blue channel image
# Blue colour is highlighted the most
cv2.imshow("Model Blue Image", b)

# Displaying Green channel image
# Green colour is highlighted the most
cv2.imshow("Model Green Image", g)

# Displaying Red channel image
# Red colour is highlighted the most
cv2.imshow("Model Red Image", r)

# Waits for user to press any key
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)

mask = cv2.bitwise_not(binary_image)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_contour_area = 100
filtered_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    print(area)
    if area >= min_contour_area:
        filtered_contours.append(contour)
color_name=['blue','green','red','organe','yello']
i=0
img_cut=[]
for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #Ex4
    img_cut.append(image[y:y+h,x:x+w])
    org= (x,y)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    color = (255, 0, 0)
    thickness = 1
    # color_name=find_color(image,x,y,x+w,y+h)
    # EX3
    cv2.putText(image, color_name[i], org, font, fontScale, color, thickness, cv2.LINE_AA)
    i=i+1
cv2.imshow('two_blobs_result.jpg',image)
cv2.waitKey(0)
print(len(img_cut))
for i in np.arange(0,len(img_cut)-1):
    cv2.imshow('Bong'+str(i),img_cut[i])
    cv2.waitKey(0)
# Ex5
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20,100,100])
upper_yellow = np.array([30,255,255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
res=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('res',res)
cv2.waitKey(0)
#Ex6
image[mask > 0] = [28,222,0]
cv2.imshow('img',image)
cv2.waitKey(0)
#Ex7
(rows, cols) = img_cut[0].shape[:2]
M = cv2.getRotationMatrix2D((cols, rows), 20, 1)
res = cv2.warpAffine(img_cut[0], M, (cols, rows))
cv2.imshow('res',res)
cv2.waitKey(0)