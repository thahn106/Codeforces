for t in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    if m == 1:
        ans = 1
    else:
        b = [0]*m
        for i in a:
            b[i%m]+=1
        for i,c in enumerate(b[:m//2+1]):
            if not i:
                if c:
                    ans +=1
            elif i == m/2:
                 if c:
                     ans +=1
            elif i<m/2:
                p,q = min(c,b[m-i]),max(c,b[m-i])
                if p or q:
                    q -= p+1
                    ans +=1
                    if q>0:
                        ans += q
    print(ans)
