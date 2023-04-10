import sys

input = sys.stdin.readline
n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
dp = [0]
for c in p:
    dp.append(dp[-1] + c)

for _ in range(q):
    x, y = map(int, input().split())
    sys.stdout.write(str((dp[n - (x - y)] - dp[n - x])) + "\n")
