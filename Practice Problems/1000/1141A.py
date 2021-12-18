n,m  = map(int, input().split())
d,r = divmod(m,n)
ans = 0
if r == 0:
    while (d%2==0):
        d /= 2
        ans+=1
    while (d%3==0):
        d /= 3
        ans +=1
if d ==1 and r ==0:
    print(ans)
else:
    print(-1)
