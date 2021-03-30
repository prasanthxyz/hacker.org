cipher = "3d2e212b20226f3c2a2a2b"
for i in range(0, len(cipher), 2):
    print(chr(int(cipher[i:i+2], 16) ^ 79), end="")
