import cv2 as cv
import numpy as np

img = cv.imread('image_3.png', cv.IMREAD_GRAYSCALE)
cv.imshow('th1',img)
cv.waitKey()

img = cv.medianBlur(img,5)
th1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv.THRESH_BINARY,11,2)

cv.imshow('th1',th1)
cv.waitKey()

kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(th1, cv.MORPH_OPEN, kernel)

cv.imshow('opening',opening)
cv.waitKey()

closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

cv.imshow('closing',closing)
cv.waitKey()

d_im = cv.dilate(closing, kernel, iterations=1)
e_im = cv.erode(d_im, kernel, iterations=1) 
cv.imshow('e_im',e_im)
cv.waitKey()

imgRGB = cv.cvtColor(e_im.copy(), cv.COLOR_GRAY2RGB)
ctrs, _ = cv.findContours(e_im, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

boxes = []
for ctr in ctrs:
    x, y, w, h = cv.boundingRect(ctr)
    boxes.append([x, y, w, h])

for box in boxes:
    top_left     = (box[0], box[1])
    bottom_right = (box[0] + box[2], box[1] + box[3])
    cv.rectangle(imgRGB, top_left, bottom_right, (0,255,0), 2)

cv.imshow("Result", imgRGB)
cv.waitKey(0)
cv.destroyAllWindows()