for t in range(int(input())):
    p = []
    for i in range(int(input())):
        x,y = map(int,input().split())
        p.append((x,y))
    p.sort()
    ans = ""
    possible = True
    x,y = 0,0
    for pi in p:
        xi, yi = pi
        if yi < y:
            possible = False
        if possible:
            ans += "R"*(xi-x)
            ans += "U"*(yi-y)
        x,y = pi
    if possible:
        print("YES")
        print(ans)
    else:
        print("NO")
