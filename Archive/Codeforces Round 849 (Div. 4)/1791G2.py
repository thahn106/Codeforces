for t in range(int(input())):
    n, C = map(int, input().split())
    a = list(map(int, input().split()))
    ref = []
    for i, c in enumerate(a):
        ref.append((c + min(i + 1, n - i), c + i + 1))
    ref.sort()
    dp = [0]
    for c, i in ref:
        dp.append(dp[-1] + c)
    ans = 0
    for i, pair in enumerate(ref):
        dis = pair[0]
        ofs = pair[1]
        k = C - ofs
        ind = 0
        if k >= 0:
            lo = 0
            hi = n
            while lo <= hi:
                mid = (lo + hi) // 2
                check = dp[mid]
                cur = mid + 1
                if mid > i:
                    check -= dis
                    cur -= 1
                if check > k:
                    hi = mid - 1
                else:
                    lo = mid + 1
                    ind = max(cur, ind)
            ans = max(ans, ind)
    # print(f"{ans=}")
    print(ans)
