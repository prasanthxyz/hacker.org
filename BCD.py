code = "0111 0011 1001 0011 1001 0001"
result = ''
for num in code.split():
    result += str(int(num, 2))
print(result)
