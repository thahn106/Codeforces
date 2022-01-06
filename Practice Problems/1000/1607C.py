for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = a[0]
    sub = 0
    for i in range(n-1):
        t = a[i]-sub
        sub += t
        ans=max (t,ans)
    ans=max (a[n-1]-sub,ans)
    print(ans)
