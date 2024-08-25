import sys
from math import ceil, gcd

input = sys.stdin.readline


def add_f(a, b):
    num = a[0] * b[1] + a[1] * b[0]
    den = a[1] * b[1]
    g = gcd(num, den)
    return (num // g, den // g)


def verify(ans, k):
    s = sum(ans)
    for bi, ki in zip(ans, k):
        if bi * ki <= s:
            return False
    return True


for t in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    sumk = (0, 1)
    for i in range(n):
        sumk = add_f(sumk, (1, k[i]))

    if sumk[0] >= sumk[1]:
        sys.stdout.write("-1\n")
        continue

    num = sumk[0]
    den = sumk[1]
    while den - num < n:
        den *= 2
        num *= 2

    ans = [0] * n
    for i in range(n):
        ans[i] = (den // k[i]) + 1

    ans[-1] = den - sum(ans[:-1])

    assert verify(ans, k)
    sys.stdout.write(" ".join(map(str, ans)) + "\n")
