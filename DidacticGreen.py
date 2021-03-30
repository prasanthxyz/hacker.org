from PIL import Image

im = Image.open('greenline.png')
pix = im.load()
greens = [pix[i,0][1] for i in range(im.size[0])]
print(''.join([chr(c) for c in greens]))
