for t in range(int(input())):
    x,y = map(int,input().split())
    x,y = max(x,y), min(x,y)
    if x==y:
        ans = 2*x
    else:
        ans = 2*y+1
        x -= y+1
        ans += 2*x
    print(ans)
