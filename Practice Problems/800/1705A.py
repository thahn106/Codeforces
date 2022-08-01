for t in range(int(input())):
    n, x = map(int, input().split())
    h = sorted(list(map(int, input().split())))
    ans = "YES"
    for i in range(n):
        if h[i]+x>h[i+n]:
            ans = "NO"
    print(ans)
