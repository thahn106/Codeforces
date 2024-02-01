import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    ans = (m // 2) * n
    if m == 1:
        print(-1)
    else:
        print(ans)
