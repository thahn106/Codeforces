for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        if i%2:
            ind = n-1-(i//2)
        else:
            ind = (i//2)
        ans.append(a[ind])
    print(*ans)
