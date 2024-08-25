import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    ma = 0
    mi = 0
    for v in x:
        if v > 0:
            ma = max(ma + v, abs(mi + v))
            mi += v
        else:
            ma = max(ma + v, abs(mi + v))
            mi += v

    print(ma)
