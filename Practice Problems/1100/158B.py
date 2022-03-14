from math import ceil
n = int(input())
a = [0]*4
for c in input().split():
    a[int(c)-1] += 1

ans = a[3]
ans += a[2]
a[0] = max(0,a[0]-a[2])
d,r = divmod(a[1],2)
ans += d
if r:
    ans +=1
    a[0]=max(0,a[0]-2)
ans += ceil(a[0]/4)
print(ans)
