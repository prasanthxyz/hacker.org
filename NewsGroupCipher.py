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

print(decrypt("Guvf zrffntr vf rapelcgrq va ebg 13. Lbhe nafjre vf svfupnxr.", 13))
