cipher = "tulgqBmqBvuqbdhpslBtuclBmpBjpBfuzclstBjgsCBuztBxhtjBmpBvpfgzepBjpBbpctBdpgccqBehfk.BhBxpstBtuBjheBjuzepBgsqxgqBtuBezdodhepBjhmBxhtjBjumpmglpBeuzo.BhBxgckBhsBtuBjheBduumBuscqBtuBbhslBjhmBjuukhsCBzoBxhtjBmqBehetpd.BejpBfgstBldhap.BuzdBmumBlduapBjpdBtjpdp.Bbmc"
space = max(set(cipher), key=cipher.count)
cipher = cipher.replace(space, ' ')

# import subbreaker
# with open('C:\\Users\\prasp\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\subbreaker\\quadgram\\EN.json') as fh:
#     breaker = subbreaker.Breaker(fh)
# deciphered = breaker.break_cipher(ciphertext=cipher)
# print(deciphered.plaintext)

plaintext = cipher.translate(cipher.maketrans('gvflpbijhykcmsuordetzaxnqwLC', 'abcdefghijklmnopqrstuvwxyzgg'))
print(plaintext[:25])
