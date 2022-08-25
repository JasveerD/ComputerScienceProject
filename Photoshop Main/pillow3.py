from PIL import Image, ImageEnhance

image = Image.open('picture.jpeg')

# creating an enhancer
color_enhancer = ImageEnhance.Color(image)  # vibrancy
contrast_enhancer = ImageEnhance.Contrast(image)  # contrast
bright_enhancer = ImageEnhance.Brightness(image)  # contrast
sharp_enhancer = ImageEnhance.Sharpness(image)  # contrast

# applying the enhancer
color_image = color_enhancer.enhance(0)
contrast_image = contrast_enhancer.enhance(5)
bright_image = bright_enhancer.enhance(5)
sharp_image = sharp_enhancer.enhance(2)


sharp_image.show()