import cv2
import numpy as np
import argparse

#Ex1
# import the necessary packages
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="img1.png",
	help="path to the input image")
args = vars(ap.parse_args())



image = cv2.imread(args["image"])
# cv2.imshow("Original", image)


mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (250, 370), 150, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)


# cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

mask_2 = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask_2, (730, 290), 150, 255, -1)
masked_2 = cv2.bitwise_and(image, image, mask=mask_2)


# cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image_2", masked_2)
cv2.waitKey(0)

mask_3 = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask_3, (1130, 430), 150, 255, -1)
masked_3 = cv2.bitwise_and(image, image, mask=mask_3)


# cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image_3", masked_3)
cv2.waitKey(0)
#Ex2
src1 = cv2.imread('img1.png')
src2 = cv2.imread('img2.png')
src2 = cv2.resize(src2, src1.shape[1::-1])
dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
cv2.imwrite('opencv_add_weighted.jpg', dst)



