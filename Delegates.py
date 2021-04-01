# 1 -> 2118
# sum of all numbers, but add squares twice
# = A: [sum of all numbers] + B: [sum of squares of all numbers until sqrt(2118)]

import math
n = 2118
sqrt_n = math.floor(math.sqrt(n))

A = n*(n+1)/2
B = sqrt_n*(sqrt_n+1)*(2*sqrt_n+1)/6
print(int(A+B))
