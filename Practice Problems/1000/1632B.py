for t in range(int(input())):
    n = int(input())
    k = 1
    while 2*k<=n-1:
        k*=2

    ans = list(range(k-1,-1,-1))+list(range(k,n))
    print(*ans)
