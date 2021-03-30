def decrypt(cipher, key):
    result = ""
    for c in cipher:
        if c.isupper():
            result += chr((ord(c) + key - 65) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) + key - 97) % 26 + 97)
        else:
            result += c

    return result

cipher = "cqrb lryqna rb fjh, fjh qjamna cqjw axc cqracnnw. qnan, hxd wnena twxf qxf oja cx bqroc! xq kh cqn fjh, cqn jwbfna rb mnjmvjwblqnbc."
# for key in range(26):
#     print(key, decrypt(cipher, key))

print(decrypt(cipher, 17))
