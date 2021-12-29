for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = [False for i in range(n)]
    ans = []
    for i in a:
        if not s[i-1]:
            s[i-1] = True
            ans.append(i)
    print(*ans)
