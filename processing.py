import imageio
imageio.plugins.ffmpeg.download()
import cv2
import numpy as np
import helpers as hp
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# for gaussian blur
kernel_size = 3

# Canny Edge Detector
low_threshold = 50
high_threshold = 150

# Region-of-interest vertices
# We want a trapezoid shape, with bottom edge at the bottom of the image
trap_bottom_width = 0.85  # width of bottom edge of trapezoid, expressed as percentage of image width
trap_top_width = 0.07  # ditto for top edge of trapezoid
trap_height = 0.4  # height of the trapezoid expressed as percentage of image height

input_file = 'maxresdefault.jpg'
image = mpimg.imread(input_file)
image = hp.filter_colors(image)

image2 = hp.grayscale(image)
image2 = hp.gaussian_blur(image2, kernel_size)

edges = cv2.Canny(image2, low_threshold, high_threshold)

# Create masked edges using trapezoid-shaped region-of-interest
imshape = image.shape
vertices = np.array([[((imshape[1] * (1 - trap_bottom_width)) // 2, imshape[0]), ((imshape[1] * (1 - trap_top_width)) // 2, imshape[0] - imshape[0] * trap_height), (imshape[1] - (imshape[1] * (1 - trap_top_width)) // 2, imshape[0] - imshape[0] * trap_height), (imshape[1] - (imshape[1] * (1 - trap_bottom_width)) // 2, imshape[0])]], dtype=np.int32)
masked_edges = hp.region_of_interest(edges, vertices)

plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
