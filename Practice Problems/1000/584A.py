n,t = [int(x) for x in input().split()]
ans =((10**(n-1))//t)*t +t
if ans >= 10**n:
    print("-1")
else:
    print(ans)
