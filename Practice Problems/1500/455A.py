n = int(input())
a = list(map(int,input().split()))
m = max(a)+1
c = [0]*(m)
for i in a:
    c[i]+=1
dpa,dpb = 0,c[1]
for i in range(2,m):
    dpc = max(dpa+c[i]*i,dpb)
    dpa=dpb
    dpb=dpc
print(dpc)
