n,m = map(int,input().split())
ans = 0
for a in range(max(n,m)+1):
    for b in range(max(n,m)+1):
        if a*a+b==n and a+b*b==m:
            ans +=1
print(ans)
