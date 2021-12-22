n,m = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = p[-1]
for i in range(m-n+1):
    ans = min(ans, p[i+n-1]-p[i])
print(ans)
