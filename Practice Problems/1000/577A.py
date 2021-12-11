n,x = [int(x) for x in input().split()]

ans = 0
for i in range(n):
    if x%(i+1)==0 and x/(i+1)<=n:
        ans+=1

print(ans)
