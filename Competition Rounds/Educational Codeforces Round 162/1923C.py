import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    dp = [0] * (n + 1)
    ones = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + c[i - 1]
        ones[i] = ones[i - 1] + (c[i - 1] == 1)

    for _ in range(q):
        l, r = map(int, input().split())
        if l == r:
            print("NO")
            continue
        total = dp[r] - dp[l - 1]
        ups = ones[r] - ones[l - 1]
        downs = total - (r - l + 1)
        if ups > downs:
            print("NO")
        else:
            print("YES")
