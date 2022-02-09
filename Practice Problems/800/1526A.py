for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    ans = []
    for i in range(n):
        ans.append(a[n+i])
        ans.append(a[i])
    print(*ans)
