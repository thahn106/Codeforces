for t in range(int(input())):
    x,n,m = map(int,input().split())
    killed = False
    while n:
        if x<=10*m:
            print("YES")
            killed = True
            break
        else:
            x = (x//2)+10
            n-=1
    if not killed:
        if x<=10*m:
            print("YES")
            killed = True
        else:
            print("NO")
