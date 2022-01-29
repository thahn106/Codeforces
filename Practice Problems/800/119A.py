from math import gcd
a,b,n = map(int,input().split())

while True:
    if n == 0:
        print(1)
        break
    else:
        n -= gcd(a,n)
    if n ==0:
        print(0)
        break
    else:
        n -= gcd(b,n)
