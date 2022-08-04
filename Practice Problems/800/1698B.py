for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k > 1:
        ans = 0 
        for i in range(1, n-1):
            if a[i] > a[i-1]+a[i+1]:
                ans += 1
        print(ans)
    else:
        print((n-1)//2)
    