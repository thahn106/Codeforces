for t in range(int(input())):
    n, m, k, H = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for x in h:
        d, r = divmod(abs(x - H), k)
        if r == 0 and 0 < d <= m - 1:
            ans += 1
    print(ans)
