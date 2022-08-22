from PIL import Image

# creating an image object
image = Image.open('picture.jpeg')

# creating an image
image_blank = Image.new('RGBA', (1000, 600))  # two arguments needed, 1st=color format, 2nd=size in pixels (tuple)

# displaying the picture
# image_blank.show()

# saving picture
# image.save('test_save.jpeg')

# image information
print(image.filename)
print(image.size)
print(image.format)
print(image.format_description)

# documentation
# https://pillow.readthedocs.io/en/stable/reference/Image.html?