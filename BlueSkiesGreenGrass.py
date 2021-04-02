from PIL import Image

im = Image.open('blueskies.png')
pix = im.load()
w, h = im.size

result = Image.new('RGB', (w, h), color = (255, 255, 255))
result_pix = result.load()

for i in range(w):
    for j in range(h):
        if pix[i, j][0] != 0:
            result_pix[i, j] = (0, 0, 0)

result.show()
