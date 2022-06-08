from math import ceil
n, k = map(int, input().split())
a = 0
for i in [2, 5, 8]:
    a += ceil(i*n/k)
print(a)
