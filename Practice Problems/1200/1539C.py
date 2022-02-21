n,k,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
difs = []
for i in range(n-1):
    d = a[i+1]-a[i]
    c = (d-1)//x
    if c>0:
        difs.append(c)

difs.sort()
ans = len(difs)+1
for d in difs:
    if d <=k:
        k-=d
        ans -=1
    else:
        break
print(ans)
