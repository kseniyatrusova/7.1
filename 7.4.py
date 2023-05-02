from PIL import Image

water = "watermark.png"
with Image.open(water) as img_water: img_water.load()

img_water = Image.open(water).convert('RGBA')
img_water = img_water.resize((img_water.width // 4, img_water.height // 4))

filename = "1.jpg"
with Image.open(filename) as img: img.load()

img.paste(img_water, (500,750),img_water)
img.save("watermark_1.jpg")


