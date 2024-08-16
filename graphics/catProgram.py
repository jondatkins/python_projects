from PIL import Image

catIm = Image.open("zophie.png")
print(catIm.size)
width, height = catIm.size
print(width)
print(height)
# print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
img = catIm.convert("RGB")
img.save("zophie.jpg")
