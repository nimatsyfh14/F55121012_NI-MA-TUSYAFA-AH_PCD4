import cv2
import numpy as np

# Load image
img = cv2.imread('nim.jpg')

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define kernel size for min filter
kernel_size = 3

# Apply min filter
kernel = np.ones((kernel_size, kernel_size), np.uint8)
min_img = cv2.erode(gray_img, kernel)

# Display original and filtered image
cv2.imshow('Original Image', gray_img)
cv2.imshow('Min Filtered Image', min_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
