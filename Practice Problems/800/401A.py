from math import ceil
n, x = map(int, input().split())
a = list(map(int, input().split()))
print(ceil(abs(sum(a))/x))
