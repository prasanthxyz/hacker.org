from PIL import Image

im = Image.open('blue.png').rotate(270, expand=1)
pix = im.load()
w, h = im.size
for i in range(w):
    for j in range(h):
        print(chr(pix[i, j][2]), end='')
    print()
