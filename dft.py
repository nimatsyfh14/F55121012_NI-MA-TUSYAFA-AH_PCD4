import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Membaca gambar dan mengonversi ke grayscale
img = Image.open('nim.jpg').convert('L')
img_arr = np.array(img)

# Menghitung DFT dari gambar
dft_output = np.fft.fft2(img_arr)
magnitude_spectrum = 20*np.log(np.abs(dft_output))

# Plot spektrum frekuensi dari gambar
plt.imshow(magnitude_spectrum, cmap='gray')
plt.axis('off')
plt.show()
