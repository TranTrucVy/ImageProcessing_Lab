import cv2
import matplotlib.pyplot as plt

image = cv2.imread("hello.jpeg")
# Convert the image to different color spaces
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Plot the original and converted images
plt.figure(figsize=(12, 6))

# Original BGR image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image (BGR)')

# Grayscale image
plt.subplot(2, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

# HSV color space
plt.subplot(2, 2, 3)
plt.imshow(hsv_image)
plt.title('HSV Color Space')

# LAB color space
plt.subplot(2, 2, 4)
plt.imshow(lab_image)
plt.title('LAB Color Space')

plt.tight_layout()
plt.show()
