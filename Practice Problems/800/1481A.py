for t in range(int(input())):
    px,py = map(int,input().split())
    U,D,R,L = 0,0,0,0
    for c in input():
        if c=="U":
            U+=1
        elif c=="D":
            D+=1
        elif c=="R":
            R+=1
        else:
            L+=1
    ans = False
    if px>=0:
        if py>=0:
            ans = px<=R and py<=U
        else:
            ans = px<=R and abs(py)<=D
    else:
        if py>=0:
            ans = abs(px)<=L and py<=U
        else:
            ans = abs(px)<=L and abs(py)<=D
    if ans:
        print("YES")
    else:
        print("NO")
