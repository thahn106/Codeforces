for t in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    ans = -1
    for i in range(n-1):
        if ans == -1:
            ans = s[i+1]-s[i]
        else:
            ans = min(ans, s[i+1]-s[i])
    print(ans)
