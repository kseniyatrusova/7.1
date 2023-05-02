from PIL import Image

a = "1.jpg"
with Image.open(a) as img:
    img.load()
img.show()

print("Ширина: ", img.size[0])
print("Высота:  ", img.size[1])
print("Цветовая модель:", img.mode)
print("Формат: ", img.format)
