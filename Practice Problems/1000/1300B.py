for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = a[-1]
    for i in range(2*n):
        ans = min(ans,  abs(a[n-1+int(i<=n-1)]-a[i]))
    print(ans)
