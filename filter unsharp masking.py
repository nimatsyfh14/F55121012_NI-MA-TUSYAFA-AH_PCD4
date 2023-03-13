import cv2
import numpy as np

# membaca gambar
img = cv2.imread('nim.jpg')

# mengaplikasikan filter unsharp masking
blur = cv2.GaussianBlur(img, (0,0), 3)
unsharp_mask = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

# menampilkan gambar asli dan hasil filter
cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Filter', unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
