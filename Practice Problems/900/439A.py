n,d = map(int,input().split())
t = list(map(int,input().split()))
ans = (d-sum(t))//5
if ans < 2*(n-1):
    print(-1)
else:
    print(ans)
