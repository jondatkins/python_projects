from PIL import Image

# /home/jon/Documents/art_graphics_etc/otherArt/heather_printed/testResize.jpg
catIm = Image.open("./inputFiles/testResize.jpg")
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save("./outputFiles/testResize.jpg")
