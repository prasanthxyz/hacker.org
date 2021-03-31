cipher = "751a6f1d3d5c3241365321016c05620a7e5e34413246660461412e5a2e412c49254a24"

result = ''
for i in range(len(cipher), 2, -2):
    byte = cipher[i-2:i]
    key = cipher[i-4:i-2]
    result += chr(int(byte, 16) ^ int(key, 16))

print(result[::-1])
