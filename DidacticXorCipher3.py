cipher = "31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588"

def lc_decrypt(cipher, b, x):
    result = decrypt(cipher, b, x)
    return ''.join([c for c in result if c.isascii() and c.islower()])

def decrypt(cipher, b, x):
    result = ''
    for i in range(0, len(cipher), 2):
        result += chr(int(cipher[i:i+2], 16) ^ b)
        b = (b + x) % 256
    return result

B = 0
X = 0
for b in range(256):
    for x in range(256):
        result = lc_decrypt(cipher, b, x)
        if len(result) > 24:
            B = b
            X = x
            break
    if B != 0:
        break

print(decrypt(cipher, B, X))
