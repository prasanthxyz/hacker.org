cipher = "310a7718781f734c31425e775a314f3b40132c5122720599b2dfb790fd8ff894add2a4bdc5d1a6e987a0ed8eee94adcfbb94ee88f382127819623a404d3f"

# Find x

# for x in range(256):
#     result = ''
#     for i in range(len(cipher), 2, -2):
#         byte = int(cipher[i-2:i], 16)
#         key = (int(cipher[i-4:i-2], 16) + x) % 0x100
#         result += chr(byte ^ key)
#     if ' ' in result and len(list(filter(lambda x:x.isascii(), result))) > 60:
#         print(x, result[::-1])

# The above code is enough to reach the solution. Just adding code with the right x and k values.

x = 249
k = 120
result = ''
for i in range(0, len(cipher), 2):
    byte = int(cipher[i:i+2], 16)
    result += chr(byte ^ k)
    k = (byte + x) % 0x100
print(result)
