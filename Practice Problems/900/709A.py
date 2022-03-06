n,b,d = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
waste = 0
for i in a:
    if i<=b:
        waste += i
        if waste>d:
            ans+=1
            waste=0
print(ans)
