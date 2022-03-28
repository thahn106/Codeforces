import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
A = [0]*100005
run = 0
dp = [0]*n
for i,e in enumerate(a[::-1]):
    if not A[e]:
        A[e]=1
        run+=1
    dp[i] = run

for i in range(m):
    e = n - int(sys.stdin.readline())
    sys.stdout.write(str(dp[e])+'\n')
sys.stdout.flush()
