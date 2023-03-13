import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Membaca gambar dan mengonversi ke grayscale
img = Image.open('nim.jpg').convert('L')
img_arr = np.array(img)

# Membuat filter highpass Ideal
def ideal_highpass_filter(shape, cutoff):
    x, y = np.meshgrid(np.arange(-shape[1]//2, shape[1]//2),
                       np.arange(-shape[0]//2, shape[0]//2))
    r = np.sqrt(x**2 + y**2)
    filter = np.zeros_like(r)
    filter[r > cutoff] = 1
    return filter

# Menghitung filter highpass Ideal dan melakukan konvolusi dengan gambar
cutoff = 30 # frekuensi cutoff
ideal_filter = 1 - ideal_highpass_filter(img_arr.shape, cutoff)
filtered_output = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(img_arr)) * ideal_filter))).real

# Menampilkan gambar hasil filterisasi
plt.imshow(filtered_output, cmap='gray')
plt.axis('off')
plt.show()
