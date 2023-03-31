import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0]
    for c in a:
        dp.append((dp[-1] + c) % 2)
    for _ in range(q):
        l, r, k = map(int, input().split())
        s = dp[n] - dp[r] + dp[l - 1] + (r - l + 1) * (k % 2)
        if s % 2:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
