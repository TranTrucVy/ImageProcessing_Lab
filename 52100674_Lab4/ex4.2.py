import cv2 as cv
import numpy as np
img = cv.imread('image_2.png', cv.IMREAD_GRAYSCALE)

img = cv.medianBlur(img,5)
th1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv.THRESH_BINARY,11,2)

cv.imshow('th1',th1)
cv.waitKey()

kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img,kernel,iterations = 1)

cv.imshow('dilation',dilation)
cv.waitKey()

closing = cv.morphologyEx(dilation, cv.MORPH_CLOSE, kernel)

cv.imshow('closing',closing)
cv.waitKey()


imgRGB = cv.cvtColor(closing.copy(), cv.COLOR_GRAY2RGB)
ctrs, _ = cv.findContours(closing, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

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
