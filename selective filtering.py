import cv2
import numpy as np

# Load gambar
img = cv2.imread('nim.jpg')

# Konversi ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Menentukan rentang warna yang akan dipertahankan (misalnya warna merah)
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# Membuat mask
mask = cv2.inRange(hsv, lower_red, upper_red)

# Aplikasi selective filtering pada gambar
result = cv2.bitwise_and(img, img, mask=mask)

# Menampilkan hasil
cv2.imshow('Selective Filtering', result)
cv2.waitKey(0)
cv2.destroyAllWindows()