from PIL import Image, ImageFilter

a = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
for i in a:
    with Image.open(i) as img:
        img.load()
        filter_img = img.filter(ImageFilter.EDGE_ENHANCE)
        filter_img.save('filter-'+i)

