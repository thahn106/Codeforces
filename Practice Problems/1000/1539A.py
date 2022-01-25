for t in range(int(input())):
    n,x,t = map(int,input().split())
    d = t // x
    if d>=n-1:
        print(n*(n-1)//2)
    else:
        print(d*n - d*(d+1)//2)
