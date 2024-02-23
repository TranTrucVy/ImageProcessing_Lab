import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection to find edges
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Perform the Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# Draw the detected lines on the original image
for rho, theta in lines[:, 0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the original image with detected lines
cv2.imwrite('HoughLineTransform.jpg', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
