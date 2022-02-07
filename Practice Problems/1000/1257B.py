for t in range(int(input())):
    x,y = map(int,input().split())
    possible = False
    if x == 1:
        if y==1:
            possible = True
    elif x == 2 or x == 3:
        if y <4:
            possible = True
    else:
        possible = True
    if possible:
        print("YES")
    else:
        print("NO")
