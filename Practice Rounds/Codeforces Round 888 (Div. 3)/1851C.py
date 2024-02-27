for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    forward = a[0]
    backward = a[-1]
    fc = 0
    fans = None
    for i, c in enumerate(a):
        if c == forward:
            fc += 1
        if fc == k:
            fans = i
            break
    bc = 0
    bans = None
    for i, c in enumerate(a[::-1]):
        if c == backward:
            bc += 1
        if bc == k:
            bans = n - 1 - i
            break
    ans = "YES"
    if forward != backward:
        if fans == None or bans == None:
            ans = "NO"
        elif fans >= bans:
            ans = "NO"
    else:
        if fans == None:
            ans = "NO"
    print(ans)
