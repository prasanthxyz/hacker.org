cipher = "8776459cf37d459fbb7b5ecfbb7f5fcfb23e478aaa3e4389f378439aa13e4e96a77b5fc1f358439df36a4486a03e4381b63e5580a66c0c8ebd6d5b8aa13e459cf34e4d9fa67f02cf90714288a17f589abf7f5886bc705fcfbc700c96bc6b5ecfb7775f8cbc68499daa3f"

def is_char(c):
    return (c == ' ') or (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z'))

keys = []
for char in range(4):
    # print("Key", char+1, end=': ')
    for key in range(256):
        result = ''
        for i in range(0, len(cipher)-(2*char), 8):
            idx = i+2*char
            result += chr(int(cipher[idx:idx+2], 16) ^ key)
        if len(list(filter(lambda x: is_char(x), result))) > 24:
            keys.append(key)
            # print(key, result)

result = ''
for i in range(0, len(cipher), 2):
    key = keys[int(i/2)%4]
    result += chr(int(cipher[i:i+2], 16) ^ key)

print(result)
