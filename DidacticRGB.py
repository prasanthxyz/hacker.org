from PIL import Image

pix = Image.open('didactrgb.png').load()
rgb = pix[0, 0]
binary = ''.join([bin(x)[2:].zfill(8) for x in rgb])
print(int(binary, 2))
