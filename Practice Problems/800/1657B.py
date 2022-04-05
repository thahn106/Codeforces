for t in range(int(input())):
    n,B,x,y = map(int,input().split())
    ans = 0
    cur = 0
    for i in range(n):
        if cur+x<=B:
            cur+=x
        else:
            cur-=y
        ans += cur
    print(ans)
