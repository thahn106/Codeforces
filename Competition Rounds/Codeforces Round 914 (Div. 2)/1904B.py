import sys

input = sys.stdin.readline


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)
    s = sum(a)
    ref = {}
    ans = n - 1
    last = b[-1]
    for i in range(n):
        ind = n - 1 - i
        if b[ind] not in ref:
            if s < last:
                ans = n - 1 - i
        ref[b[ind]] = ans
        last = b[ind]
        s -= b[ind]
    ans = [ref[i] for i in a]
    print(*ans)
