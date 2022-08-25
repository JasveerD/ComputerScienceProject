from PIL import Image, ImageColor

image = Image.open('picture.jpeg')

# rotating
# argument:(angle, not be cropped at the edges, bcgk color returns a tuple with RGB values
image_rotate = image.rotate(60, expand=True, fillcolor=ImageColor.getcolor('red', 'RGB'))

# cropping
# image.crop((left_x, top_y, right_x, bottom_y))
image_crop = image.crop((0, 0, 500, 400))

# flipping the image
image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

# resize
image_resized = image.resize((1000, 1000))  # arg = tuple

# better resizing
scale_factor = 2
new_image_size = (image.size[0] * scale_factor, image.size[1] * scale_factor)
better_resized_image = image.resize(new_image_size)

better_resized_image.show()
