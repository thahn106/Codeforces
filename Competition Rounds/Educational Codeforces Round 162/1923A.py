import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    start = False
    ans = 0
    cur = 0
    for x in a:
        if x == 1:
            start = True
            ans += cur
            cur = 0

        if start and x == 0:
            cur += 1
    print(ans)
