from PIL import Image

img = Image.open('test.jpg')

img = img.resize((225, 225))

img.save('resized_test.jpg')

