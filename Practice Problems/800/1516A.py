for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(0,n-1):
        d = min(k,a[i])
        a[i]-=d
        a[-1]+=d
        k -= d
        if k==0:
            break
    print(*a)
