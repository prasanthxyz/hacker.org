# Brute-Force. Gotta find a better way

import itertools
import urllib.parse

code = "cXVlZW4lMjdzJTIwZ2FtYml0"
keyStr = "ABCDEFGHIJKLMNOP" + "QRSTUVWXYZabcdef" + "ghijklmnopqrstuv" + "wxyz0123456789+/" + "="

def encodeIt(text):
    # handle the url encoding part in the logic itself => % and digits
    # text = urllib.parse.quote_plus(text)
    # text = text.replace('+', '%20')
    output = ''
    chr1 = chr2 = chr3 = ''
    enc1 = enc2 = enc3 = enc4 = ''
    i = 0

    while True:
        chr1 = ord(text[i])
        i += 1
        chr2 = 0
        if i < len(text):
            chr2 = ord(text[i])
            i += 1
        chr3 = 0
        if i < len(text):
            chr3 = ord(text[i])
            i += 1
        # print([chr(x) for x in [chr1, chr2, chr3]])

        enc1 = chr1 >> 2
        enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
        enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
        enc4 = chr3 & 63

        if chr2 == 0:
            enc3 = enc4 = 64
        elif chr3 == 0:
            enc4 = 64

        output = output + keyStr[enc1] + keyStr[enc2] + keyStr[enc3] + keyStr[enc4]
        chr1 = chr2 = chr3 = 0
        enc1 = enc2 = enc3 = enc4 = 0
        if i >= len(text):
            break

    return output

charset = 'abcdefghijklmnopqrstuvwxyz%1234567890'
def decodeChunk(code):
    resultList = [list(charset), ['x'], ['x']]

    for iteration in range(3):
        combinations = itertools.product(*resultList)
        temp = []
        for c in combinations:
            text = ''.join(c)
            if code.startswith(encodeIt(text)[:iteration+1]):
                temp.append(text[iteration])
        resultList[iteration] = temp[:]
        if iteration != 2:
            resultList[iteration+1] = list(charset)

    combinations = itertools.product(*resultList)
    for c in combinations:
        text = ''.join(c)
        if encodeIt(text) == code:
            return text
    return ''

# def decodeChunk(code):
#     resultList = [charset, charset, charset]
#     combinations = itertools.product(*resultList)
#     for c in combinations:
#         text = ''.join(c)
#         if encodeIt(text) == code:
#             return text
#     return ''

result = ''
for i in range(0, len(code), 4):
    code_chunk = code[i:i+4]
    result += decodeChunk(code[i:i+4])

print(urllib.parse.unquote(result))
