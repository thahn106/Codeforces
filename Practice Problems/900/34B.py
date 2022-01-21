n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
for i in a[:m]:
    if i<0:
        ans -= i
print(ans)
