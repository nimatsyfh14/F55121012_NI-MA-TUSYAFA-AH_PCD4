import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Membaca gambar dan mengonversi ke grayscale
img = Image.open('nim.jpg').convert('L')
img_arr = np.array(img)

# Membuat filter highpass Butterworth
def butterworth_highpass_filter(shape, cutoff, order):
    x, y = np.meshgrid(np.arange(-shape[1]//2, shape[1]//2),
                       np.arange(-shape[0]//2, shape[0]//2))
    r = np.sqrt(x**2 + y**2)
    filter = 1 / (1 + (r/cutoff)**(2*order))
    return filter

# Menghitung filter highpass Butterworth dan melakukan konvolusi dengan gambar
cutoff = 30 # frekuensi cutoff
order = 2 # orde filter
butterworth_filter = 1 - butterworth_highpass_filter(img_arr.shape, cutoff, order)
filtered_output = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(img_arr)) * butterworth_filter))).real

# Menampilkan gambar hasil filterisasi
plt.imshow(filtered_output, cmap='gray')
plt.axis('off')
plt.show()
