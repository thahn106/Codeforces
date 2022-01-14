for t in range(int(input())):
    a,b,c = map(int,input().split())
    s = min(a,b)
    e = max(a,b)
    if s > e-s:
        print(-1)
    else:
        if c> 2*(e-s):
            print(-1)
        elif c<=e-s:
            print(c+e-s)
        else:
            print(c-e+s)
