for q in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 1
    for i in range(n-1):
        if a[i+1]-a[i]==1:
            ans = 2
    print(ans)
