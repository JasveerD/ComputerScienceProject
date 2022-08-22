from PIL import Image, ImageColor

image = Image.open('picture.jpeg')

# rotating
# argument:(angle, not be cropped at the edges, bcgk color returns a tuple with RGB values
image_rotate = image.rotate(60, expand=True, fillcolor=ImageColor.getcolor('red', 'RGB'))

# cropping
# image.crop((left_x, top_y, right_x, bottom_y))
image_crop = image.crop((0, 0, 500, 400))

# flipping the image

