d,st = map(int,input().split())
mi = []
ma = []
for i in range(d):
    mit,mat = map(int,input().split())
    mi.append(mit)
    ma.append(mat)

if not sum(mi)<=st<=sum(ma):
    print("NO")
else:
    print("YES")
    ans = []
    s = st-sum(mi)
    for i in range(d):
        if s:
            dr = min(s, ma[i]-mi[i])
            ans.append(mi[i]+dr)
            s-=dr
        else:
            ans.append(mi[i])
    print(*ans)
