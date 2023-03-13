import cv2
import numpy as np

# membaca gambar
img = cv2.imread('nim.jpg', 0)

# mengaplikasikan filter highpass dengan kernel Gaussian
kernel_size = (5, 5)
sigma = 1.5
kernel = cv2.getGaussianKernel(kernel_size[0], sigma) * cv2.getGaussianKernel(kernel_size[1], sigma).T
highpass = cv2.filter2D(img, -1, kernel)

# menampilkan gambar asli dan hasil filter
cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Filter', highpass)
cv2.waitKey(0)
cv2.destroyAllWindows()
