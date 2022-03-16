n,k = map(int,input().split())
h = list(map(int,input().split()))

run = sum(h[:k])
dp = [run]
for i in range(k,n):
    run += h[i]-h[i-k]
    dp.append(run)

ans = 0
m = 150000000
for i,c in enumerate(dp):
    if c<m:
        m = c
        ans = i
print(ans+1)
