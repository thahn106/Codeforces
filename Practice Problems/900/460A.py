n,m = map(int,input().split())
q,d = divmod(n,(m-1))
ans = q*m+d
if not d:
    ans -=1
print(ans)
