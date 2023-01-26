from math import sqrt, gcd
from random import randrange

# miller_rabin tes
def miller_rabin(n, a):
    # n-1 = d*2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d = d // 2

    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for i in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


# Miller deterministic primality test implementation
# Pick prime list depending on size of tested number
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    prime_list = [2, 7, 61]  # 32-bit version, works up to 4,759,123,141>2**32
    for p in prime_list:
        if n == p:
            return True
        if not miller_rabin(n, p):
            return False
    return True


# find a prime factor of n
def pollard_rho(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = randrange(2, n)
    y = x
    c = randrange(1, n)
    d = 1
    while d == 1:
        x = ((x**2 % n) + c + n) % n
        y = ((y**2 % n) + c + n) % n
        y = ((y**2 % n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            x = randrange(2, n)
            y = x
            c = randrange(1, n)
    if is_prime(d):
        return d
    else:
        return pollard_rho(d)


def factorize(n):
    factors = []
    while n > 1:
        divisor = pollard_rho(n)
        factors.append(divisor)
        k, r = divmod(n, divisor)
        while not r:
            n = k
            k, r = divmod(k, divisor)
    factors.sort()  # Optional sort
    return factors


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    seen = set()
    found = False
    for x in a:
        if x == 1:
            continue
        divs = factorize(x)
        last = 0
        for p in divs:
            if p != last:
                if p in seen:
                    found = True
                    break
                else:
                    seen.add(p)
                    last = p
        if found:
            break

    if found:
        print("YES")
    else:
        print("NO")
