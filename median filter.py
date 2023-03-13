import cv2
import numpy as np

# Load image
img = cv2.imread('nim.jpg')

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define kernel size for median filter
kernel_size = 3

# Apply median filter
median_img = cv2.medianBlur(gray_img, kernel_size)

# Display original and filtered image
cv2.imshow('Original Image', gray_img)
cv2.imshow('Median Filtered Image', median_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
