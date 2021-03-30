from PIL import Image

im = Image.open('redeye.jpg')
pix = im.load()
width, height = im.size
for i in range(width):
    for j in range(height):
        r, g, b = pix[i, j]
        pix[i, j] = (r, 0, 0)
im.save('redeye_solution.jpg')
