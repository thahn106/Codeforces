for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        ans += max(0, a[i]-a[i+1])

    print(ans)
