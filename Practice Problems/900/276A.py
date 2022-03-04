n,k = map(int,input().split())
ans = None
for i in range(n):
    f,t = map(int,input().split())
    ta = f-max(0,t-k)
    if ans is None:
        ans = ta
    else:
        ans = max(ans, ta)
print(ans)