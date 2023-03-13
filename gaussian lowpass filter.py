import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Membaca gambar dan mengonversi ke grayscale
img = Image.open('nim.jpg').convert('L')
img_arr = np.array(img)

# Membuat filter lowpass Gaussian
def gaussian_lowpass_filter(shape, cutoff):
    x, y = np.meshgrid(np.arange(-shape[1]//2, shape[1]//2),
                       np.arange(-shape[0]//2, shape[0]//2))
    r = np.sqrt(x**2 + y**2)
    filter = np.exp(-(r**2) / (2 * (cutoff**2)))
    return filter

# Menghitung filter lowpass Gaussian dan melakukan konvolusi dengan gambar
cutoff = 50 # frekuensi cutoff
gaussian_filter = gaussian_lowpass_filter(img_arr.shape, cutoff)
filtered_output = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(img_arr)) * gaussian_filter))).real

# Menampilkan gambar hasil filterisasi
plt.imshow(filtered_output, cmap='gray')
plt.axis('off')
plt.show()
