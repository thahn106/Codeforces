from math import sqrt

MAXP = 1000000
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

for t in range(int(input())):
    n,k =map(int,input().split())
    j = 0
    while n%primes[j]:
        j+=1
    n+=primes[j]
    k -= 1
    n+=2*k
    print(n)
