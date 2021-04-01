"""
# Recursive with memoization
# Calling from lower numbers up to get results into the dict

d = {}

def calc(depth):
    if depth == 0:
        return 1

    if depth in d:
        return d[depth]

    cc = calc(depth-1)
    X = 1 if (cc^depth) % 4 == 0 else 0
    d[depth] = cc + (depth%7) + X
    return d[depth]

for i in range(11589):
    calc(i)

print(calc(11589))
"""

# Iterative
results = [1]
for depth in range(1, 11589+1):
    cc = results[depth-1]
    X = 1 if (cc^depth) % 4 == 0 else 0
    results.append(cc + depth%7 + X)

print(results[-1])
