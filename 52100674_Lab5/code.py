import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ex5.1: Image histogram equalization
# Load your image
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# 1. Show image histogram (gray)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Image Histogram')
plt.show()

# 2. Enhance image contrast by histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ex5.2: Image blurring
# 3. Add some noise to the input image
noisy_image = image + np.random.normal(0, 50, image.shape).astype(np.uint8)

# 4. Blur the image by using at least 5 different techniques
blurred1 = cv2.GaussianBlur(noisy_image, (5, 5), 0)
blurred2 = cv2.medianBlur(noisy_image, 5)
blurred3 = cv2.bilateralFilter(noisy_image, 9, 75, 75)
blurred4 = cv2.blur(noisy_image, (5, 5))
blurred5 = cv2.boxFilter(noisy_image, -1, (5, 5))

# Display the noisy and blurred images
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Blurred Image 1', blurred1)
cv2.imshow('Blurred Image 2', blurred2)
cv2.imshow('Blurred Image 3', blurred3)
cv2.imshow('Blurred Image 4', blurred4)
cv2.imshow('Blurred Image 5', blurred5)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ex5.3: Image sharpening
# Sharpen the input image by using at least 2 different techniques

# Technique 1: Using filter2D
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])
sharpened_image1 = cv2.filter2D(image, -1, kernel)

# Technique 2: Using addWeighted
sharpened_image2 = cv2.addWeighted(image, 1.5, image, -0.5, 0)

# Display the sharpened images
cv2.imshow('Sharpened Image 1', sharpened_image1)
cv2.imshow('Sharpened Image 2', sharpened_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
