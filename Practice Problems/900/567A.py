n = int(input())
x = list(map(int,input().split()))
a = sorted(zip(x,range(n)))

minl = [0]*n
maxl = [0]*n

MAXN = 10**10

for i in range(n):
    d,ind = a[i]
    left = MAXN
    right = MAXN
    if i >0:
        left = abs(a[i-1][0]-d)
    if i < n-1:
        right = abs(a[i+1][0]-d)
    ma = max(abs(a[0][0]-d),abs(a[-1][0]-d))
    mi = min(left,right)
    minl[ind]=mi
    maxl[ind]=ma

for i in range(n):
    print(minl[i],maxl[i])
