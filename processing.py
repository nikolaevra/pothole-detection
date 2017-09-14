from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

# import image
#img = Image.open('image.png')

# crop
#area = (0, 580, 1980, 1080)
#img = img.crop(area)
#img.save('cropped.png')

# convert to greyscale
# img = img.convert('LA')
# img.save('greyscale.png')


img = cv2.imread('maxresdefault.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
