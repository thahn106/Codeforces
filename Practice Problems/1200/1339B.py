for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = []
    start = 0
    end = n-1
    while start <=end:
        ans.append(a[start])
        start+=1
        if start <= end:
            ans.append(a[end])
            end -= 1
    ans.reverse()
    print(*ans)
