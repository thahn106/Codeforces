for t in range(int(input())):
    n,k = map(int,input().split())
    if n%3==0:
        a,b,c = n//3,n//3,n//3
    elif n%2==0:
        if n%4==0:
            a,b,c = n//2, n//4, n//4
        else:
            a,b,c = (n-2)//2,(n-2)//2,2
    else:
        a,b,c = (n-1)//2,(n-1)//2,1
    print("{} {} {}".format(a,b,c))
