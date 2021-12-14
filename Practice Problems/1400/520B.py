n, m = map(int, input().split())
ans=0
while(n!=m):
    if m<n or m%2==1:
        m += 1
    else:
        m = m//2
    ans+=1
print(ans)
