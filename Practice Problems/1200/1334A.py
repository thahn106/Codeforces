for t in range(int(input())):
    a,b = 0,0
    possible =True
    for n in range(int(input())):
        c,d = map(int,input().split())
        if d-b > c-a or d<b or c<a:
            possible=False
        a,b = c,d
    if possible:
        print("YES")
    else:
        print("NO")
