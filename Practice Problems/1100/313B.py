import sys

s = list(input())
dp = [0]*len(s)
run = 0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        run+=1
    dp[i]=run

for m in range(int(input())):
    l,r = map(int,sys.stdin.readline().split())
    sys.stdout.write(str(dp[r-1]-dp[l-1])+'\n')
sys.stdout.flush()
