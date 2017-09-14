from PIL import Image

# import image
img = Image.open('image.png')

# crop
area = (0, 580, 1980, 1080)
img = img.crop(area)
img.save('cropped.png')

# convert to greyscale
# img = img.convert('LA')
# img.save('greyscale.png')

