from bisect import bisect_left
from math import ceil


# miller_rabin test
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
    # prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]  # 64-bit version
    for p in prime_list:
        if n == p:
            return True
        if not miller_rabin(n, p):
            return False
    return True


# find a prime factor of n
def pollard_rho(n):
    from random import randrange
    from math import gcd

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
        n = n // divisor
    return factors


factorization = []


def get_factors(depth):
    p, exp = factorization[depth]
    powlist = [p**i for i in range(exp + 1)]
    if depth == len(factorization) - 1:
        return powlist
    next = get_factors(depth + 1)
    return [d1 * d2 for d1 in powlist for d2 in next]


for t in range(int(input())):
    n, m1, m2 = map(int, input().split())
    m = m1 * m2
    if m == 1:
        print(1, 1)
        continue
    factors = []
    if m1 > 1:
        factors += factorize(m1)
    if m2 > 1:
        factors += factorize(m2)
    factors.sort()

    factorization = []
    cur = factors[0]
    cc = 0
    for p in factors:
        if p == cur:
            cc += 1
        else:
            if cc:
                factorization.append((cur, cc))
            cur = p
            cc = 1
    factorization.append((cur, cc))
    divs = get_factors(0)
    divs.sort()

    count = 0
    ans = 0
    found = set()

    N = len(divs)
    for d in divs:
        i = bisect_left(divs, ceil(d / n))
        while i < N and divs[i] <= n:
            if d % divs[i] == 0:
                count += 1
                ans = ans ^ divs[i]
                break
            i += 1
    print(count, ans)
