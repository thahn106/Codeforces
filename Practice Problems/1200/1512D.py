for t in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    b.sort()
    s = sum(b[:-1])
    ind = -1
    for i in range(n):
        if s-b[i]==b[-1]:
            ind = i
            break
    if ind == -1:
        if s-b[n] in b[n:]:
            ind = n
    if ind == -1:
        print(-1)
    else:
        ans = b[:-1]
        ans.pop(ind)
        print(*ans)
