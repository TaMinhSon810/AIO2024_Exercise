import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('AIO2024_Exercise/Module_2/Week_1/dog.jpeg')

# Lightness
max_channel = np.max(img, axis=2)
min_channel = np.min(img, axis=2)
gray_method_1 = (max_channel + min_channel) / 2
gray_method_1[0, 0]

# Average
gray_method_2 = np.mean(img, axis=2)
gray_method_2[0, 0]

# Luminosity
gray_method_3 = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
gray_method_3[0, 0]

# Display image
plt.imshow(gray_method_3, cmap='gray')
plt.axis('off')
plt.show()
