for q in range(int(input())):
    a,b,n,S = map(int,input().split())
    cur = a*n+b
    if S <= cur:
        x = min((cur-S)//n,a)
        cur -= x*n
        if b >= cur-S:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
