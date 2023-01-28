from math import gcd
from functools import reduce

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = reduce(gcd, a)
    if d == 1:
        print(0)
    elif len(a) == 1:
        print(1)
    else:
        if gcd(d, n) == 1:
            print(1)
        elif gcd(d, n - 1) == 1:
            print(2)
        else:
            print(3)
