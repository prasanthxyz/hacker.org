cipher = "948881859781c4979186898d90c4c68c85878f85808b8b808881c6c4828b96c4908c8d97c4878c858888818a8381"

for key in range(256):
    result = ''
    for i in range(0, len(cipher), 2):
        result += chr(int(cipher[i:i+2], 16) ^ key)
    if len(list(filter(lambda x: x.isascii() and x.islower(), result))) > 38:
        print(result)
