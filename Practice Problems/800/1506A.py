for t in range(int(input())):
    n,m,x = map(int,input().split())
    r,c = divmod(x-1,n)
    print(c*m+r+1)
