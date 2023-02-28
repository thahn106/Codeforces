for t in range(int(input())):
    n, C = map(int, input().split())
    a = list(map(int, input().split()))
    ref = []
    for i, c in enumerate(a):
        ref.append(c + i + 1)
    ref.sort()
    dp = [0]
    for c in ref:
        dp.append(dp[-1] + c)
    lo = 0
    hi = n
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        check = dp[mid]
        if check > C:
            hi = mid - 1
        else:
            lo = mid + 1
            ans = max(mid, ans)
    print(ans)
