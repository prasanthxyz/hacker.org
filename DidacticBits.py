cipher = "abbbabaaabbabaaaabbaababaabaaaaaabbaaaababbabbbaabbbaabbabbbabbbabbaabababbbaabaaabaaaaaabbabaababbbaabbaabaaaaaabbaaaababbaabaaabbbabababbabbababbaaabaabbbaabaabbaaaababbbabaaabbaabab"
cipher = cipher.replace('a', '0').replace('b', '1')

chars = [cipher[i:i+8] for i in range(0, len(cipher), 8)]
print(''.join([chr(int(c, 2)) for c in chars]))
