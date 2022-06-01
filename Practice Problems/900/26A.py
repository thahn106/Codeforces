from math import sqrt
MAXP = 3000
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

n = int(input())
ans = 0
for i in range(6, n+1):
    for p in primes:
        if i % p == 0:
            while not i % p:
                i = i // p
            for q in primes:
                if i % q == 0:
                    while not i % q:
                        i = i // q
                    if i == 1:
                        ans +=1
                    break
            break
print(ans)
