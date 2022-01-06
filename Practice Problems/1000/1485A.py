for t in range(int(input())):
    a,b = map(int,input().split())
    ans = 40
    for i in range(max(0,2-b), 31):
        t = i
        at = a
        while at:
            t+=1
            at = at // (b+i)
        ans = min(ans,t)
    print(ans)
