n,q = map(int,input().split())
s = input()

dp = [0]
run = 0
for c in s:
    run+=ord(c)-96
    dp.append(run)

for i in range(q):
    l,r = map(int,input().split())
    print(dp[r]-dp[l-1])
