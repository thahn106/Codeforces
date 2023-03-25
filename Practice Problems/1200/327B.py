def sieve(MAXP):
    primes = [2]
    sieve = [0] * ((MAXP) // 2)
    for i in range(1, MAXP // 2):
        if not sieve[i]:
            p = 2 * i + 1
            primes.append(p)
            cur = p
            ind = i
            tp = p * 2
            while cur < MAXP:
                sieve[ind] = 1
                ind += p
                cur += tp
    return primes


primes = sieve(1300000)


n = int(input())
print(*primes[:n])
