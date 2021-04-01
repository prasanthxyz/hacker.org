nterms = 1500000
a, b = 0, 1
count = 0
while count < nterms:
    # print(a)
    c = a + b
    a = b
    b = c
    count += 1

big_fib = str(a)

result = ''
for i in range(0, len(big_fib), 20000):
    result += big_fib[i]

print(result)
