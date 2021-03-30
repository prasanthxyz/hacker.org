# import subbreaker
# with open('C:\\Users\\prasp\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\subbreaker\\quadgram\\EN.json') as fh:
#     breaker = subbreaker.Breaker(fh)

cipher = "ISS NVVK DIPXYWA PIT AVSUY QIAOP PWZEHVNWIEDZ. CDYT ZVM LOTK HDY AVSMHOVT HV HDOA HYFH, ZVM COSS QY IQSY HV NYH HDY ITACYW, CDOPD OA IKMGQWIHY."
# plaintext = breaker.break_cipher(ciphertext=cipher)
# print(plaintext.plaintext)
print(cipher.translate(cipher.maketrans('IQPKYLNDOJXSGTVERWAHMUCFZB', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
