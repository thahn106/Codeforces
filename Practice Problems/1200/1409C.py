for t in range(int(input())):
    n,x,y=map(int,input().split())
    ans = y*50
    for j in range(1,n):
        for i in range(0,j):
            q,r = divmod((y-x),(j-i))
            if r==0:
                start = y-j*q
                if start >0 and ((n-1-j)*q+y) < ans:
                    a,b = start, q
    ans = [a+b*i for i in range(n)]
    print(*ans)
