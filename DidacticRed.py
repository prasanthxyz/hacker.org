from PIL import Image

im = Image.open('redline.png')
pix = im.load()
reds = [pix[i,0][0] for i in range(im.size[0])]
print(''.join([hex(x)[2:] for x in reds]))
