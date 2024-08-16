from PIL import Image

catIm = Image.open("./inputFiles/testResize.jpg")
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save("./outputFiles/quarterHeather.jpg")
svelteIm = catIm.resize((width, height + 300))
svelteIm.save("./outputFiles/svelteHeather.jpg")
