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
    factors.sort()  # Optional sort
    return factors


for t in range(int(input())):
    n = int(input())
    factors = factorize(n)
    cur = None
    count = 0
    ref = []
    for p in factors:
        if cur == p:
            count += 1
        else:
            if cur is not None:
                ref.append((count, cur))
            cur = p
            count = 1
    ref.append((count, cur))
    ref.sort(reverse=True)
    ans = 0
    i = 1
    while True:
        cur = 1
        for count, p in ref:
            if count < i:
                break
            cur *= p

        if cur == 1:
            break

        ans += cur
        i += 1
    print(ans)
