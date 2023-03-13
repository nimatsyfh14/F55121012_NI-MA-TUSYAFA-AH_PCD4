import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Membaca gambar dan mengonversi ke grayscale
img = Image.open('nim.jpg').convert('L')
img_arr = np.array(img)

# Menghitung transformasi Fourier dari gambar
f = np.fft.fft2(img_arr)
fshift = np.fft.fftshift(f)

# Membuat filter Laplacian
rows, cols = img_arr.shape
crow, ccol = rows//2, cols//2
mask = np.zeros((rows,cols), np.uint8)
mask[crow-1:crow+2, ccol-1:ccol+2] = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], np.uint8)

# Mengaplikasikan filter pada gambar pada domain frekuensi
fshift = fshift * mask
f_ishift = np.fft.ifftshift(fshift)
img_filtered = np.fft.ifft2(f_ishift).real

# Menampilkan gambar hasil filterisasi
plt.imshow(img_filtered, cmap='gray')
plt.axis('off')
plt.show()
