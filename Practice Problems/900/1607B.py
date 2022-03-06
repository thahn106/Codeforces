for t in range(int(input())):
    x,n = map(int,input().split())

    i = (n//4)*4+1
    while i<=n:
        if x%2:
            x += i
        else:
            x -= i
        i+=1
    print(x)
