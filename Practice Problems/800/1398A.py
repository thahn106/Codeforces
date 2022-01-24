for t in range(int(input())):
    n = int(input())
    a = list(zip(list(map(int,input().split())),range(n)))
    a.sort()
    if a[0][0]+a[1][0]<=a[n-1][0]:
        ans = [a[0][1]+1,a[1][1]+1,a[n-1][1]+1]
        ans.sort()
        print(*ans)
    else:
        print(-1)
