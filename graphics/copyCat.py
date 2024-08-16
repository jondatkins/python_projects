from PIL import Image

catIm = Image.open("./inputFiles/testResize.jpg")
catCopyIm = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
print(faceIm.size)
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save("./outputFiles/tiled.jpg")
