for t in range(int(input())):
    r,g,b,w = map(int,input().split())
    possible = False
    s = (r%2)+(g%2)+(b%2)+(w%2)
    if s == 0 or s == 1:
        possible = True
    elif s==3 or s == 4:
        if r>0 and g>0 and b>0:
            possible = True
    if possible:
        print("Yes")
    else:
        print("No")
