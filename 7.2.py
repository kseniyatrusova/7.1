from PIL import Image

a = "1.jpg"
with Image.open(a) as img:
    img.load()

img1 = img.resize((img.width // 3, img.height // 3))
img1.save('1-1.jpg')
img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
img2.save('1-2.jpg')
img3.save('1-3.jpg')
