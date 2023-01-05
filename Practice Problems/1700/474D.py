MOD = 10**9+7

t,k = map(int, input().split())
dp = [0]*100005
dp[0] = 1
for i in range(1, 100001):
    dp[i] = dp[i-1]
    if i>=k:
        dp[i] = (dp[i]+dp[i-k]%MOD)

dps = [0]*100005
run = 0
for i in range(1, 100001):
    run = (run+dp[i])%MOD
    dps[i] = run

for _ in range(t):
    a,b = map(int, input().split())
    print((dps[b]-dps[a-1])%MOD)