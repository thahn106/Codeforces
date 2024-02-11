import sys

input = sys.stdin.readline


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
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]  # 64-bit version
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
    factors.sort()
    return factors


def condense_factors(factor_list):
    factors = []
    prime = 0
    power = 0
    for p in factor_list:
        if p == prime:
            power += 1
        else:
            if prime:
                factors.append((prime, power))
            prime = p
            power = 1
    else:
        if prime:
            factors.append((prime, power))
    return factors


def get_factors(factor_list):
    if not factor_list:
        yield 1
        return
    n = len(factor_list)
    pos = 0
    pstack = [0] * n
    vstack = [1] * n

    cur = 1
    curp = 0
    while True:
        if pos == n:
            yield cur
            pos -= 1
            curp = pstack[pos]
            cur = vstack[pos]
            curp += 1
            cur *= factor_list[pos][0]
        elif curp <= factor_list[pos][1]:
            pstack[pos] = curp
            vstack[pos] = cur
            pos += 1
            curp = 0
        elif pos:
            pos -= 1
            curp = pstack[pos]
            cur = vstack[pos]
            curp += 1
            cur *= factor_list[pos][0]
        else:
            break


def gen(n, k):
    r = n % (2 * k - 2)
    return min(r, 2 * k - 2 - r)


for t in range(int(input())):
    n, x = map(int, input().split())
    n -= 1
    x -= 1
    if (n - x) % 2:
        print(0)
        continue
    ans = 0
    s = set()
    facs = condense_factors(factorize((n - x) // 2))
    for cand in get_factors(facs):
        # cand = k-1
        k = cand + 1
        if k <= x:
            continue
        s.add(k)
    facs = condense_factors(factorize((n + x) // 2))
    for cand in get_factors(facs):
        # cand = k-1
        k = cand + 1
        if k <= x:
            continue
        s.add(k)

    print(len(s))
    # for c in s:
    #     print(c, gen(n, c))
