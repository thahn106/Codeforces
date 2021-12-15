import math
from functools import reduce

def lgcd(list):
    x = reduce(math.gcd, list)
    return x

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    first = a[0::2]
    second = a[1::2]
    possible = True
    tg = lgcd(first)
    for x in second:
        if x%tg==0:
            possible=False
    if not possible:
        possible =  True
        tg=lgcd(second)
        for x in first:
            t = math.gcd(x, tg)
            if x%tg==0:
                possible=False
    if not possible:
        print(0)
    else:
        print(tg)
