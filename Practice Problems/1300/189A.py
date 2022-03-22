n,a,b,c = map(int,input().split())
s = [a,b,c]
dp = [0] * (n+1)
for i in s:
    if i<=n:
        dp[i]=1
for i,e in enumerate(dp):
    if e:
        for a in s:
            if i+a<=n:
                dp[i+a]=max(dp[i+a],dp[i]+1)
print(dp[n])
