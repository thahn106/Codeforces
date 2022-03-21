from math import sqrt, floor
from bisect import bisect_left

n = int(input())
x = list(map(int,input().split()))

MAXP = floor(sqrt(max(x)))+3
primes = [2,3,5,7,11,13,17,19]
for n in range(21, MAXP,2):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n%p == 0:
            prime = False
            break
    if prime:
        primes.append(n)

for i in x:
    s = floor(sqrt(i))
    ind = bisect_left(primes,s)
    if sqrt(i)==s and ind< len(primes) and primes[ind]==s:
        print("YES")
    else:
        print("NO")
