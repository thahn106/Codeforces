import sys

input = sys.stdin.readline


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = max(a) - 1

    for i in range(1, n):
        ans = min(ans, max(a[i] - 1, a[i - 1] - 1))

    print(ans)
