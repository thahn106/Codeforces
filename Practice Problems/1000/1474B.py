from math import sqrt
primes  = [2,3,5,7,11,13]

for n in range(17,30000,2):
    prime = True
    i=0
    while i < len(primes):
        p = primes[i]
        if n%p==0:
            prime = False
        if p > sqrt(n):
            i = len(primes)
        i+=1
    if prime:
        primes.append(n)

for t in range(int(input())):
    d = int(input())
    first = False
    i = 0
    while not first:
        if (primes[i]-1)>= d:
            first = primes[i]
        i+=1
    second = False
    while not second:
        if (primes[i]-first)>= d:
            second = primes[i]
        i+=1
    print(first*second)
