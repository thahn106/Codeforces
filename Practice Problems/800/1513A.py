for t in range(int(input())):
    n,k = map(int,input().split())
    if 2*k<n:
        ans = []
        for i in range(k):
            ans += [i+1,n-i]
        ans += list(range(k+1,n-k+1))
        print(*ans)
    else:
        print(-1)
