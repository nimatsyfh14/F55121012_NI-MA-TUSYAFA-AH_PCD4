import cv2
import numpy as np

# Load image
img = cv2.imread('nim.jpg')

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define kernel size for max filter
kernel_size = 3

# Apply max filter
kernel = np.ones((kernel_size, kernel_size), np.uint8)
max_img = cv2.dilate(gray_img, kernel)

# Display original and filtered image
cv2.imshow('Original Image', gray_img)
cv2.imshow('Max Filtered Image', max_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
