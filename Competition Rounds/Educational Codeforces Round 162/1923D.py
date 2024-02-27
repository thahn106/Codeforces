import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * (n + 1)

    ndr = [None] * n  # next different element on the right
    ndl = [None] * n  # next different element on the left

    cur = a[0]
    run = 0
    for i, x in enumerate(a):
        dp[i + 1] = dp[i] + x
        if x != cur:
            for j in range(run, i):
                ndr[j] = i
            run = i
            cur = x

    cur = a[-1]
    run = n - 1
    for i in range(n - 1, -1, -1):
        if a[i] != cur:
            for j in range(run, i, -1):
                ndl[j] = i
            run = i
            cur = a[i]

    def nm(a, b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    # DEBUG = True
    # if DEBUG:
    #     print("dp:", dp)
    #     print("ndl:", ndl)
    #     print("ndr:", ndr)

    ans = [-1] * n
    for i in range(n):
        # left eat
        value = a[i]
        if i > 0 and a[i - 1] > a[i]:
            ans[i] = 1
            continue
        if i < n - 1 and a[i] < a[i + 1]:
            ans[i] = 1
            continue

        left_turns = None
        if i > 0 and ndl[i - 1] is not None and dp[i] - dp[0] > value:
            lo = 0
            hi = i
            # print("Left: i, lo, hi", i, lo, hi)
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if dp[i] - dp[mid] > value:
                    lo = mid
                else:
                    hi = mid
                pass

            ind = min(lo, ndl[i - 1])
            # print("i, ind: ", i, ind)
            left_turns = i - ind

        right_turns = None
        if i < n - 1 and ndr[i] is not None and dp[n] - dp[i + 1] > value:
            lo = i
            hi = n - 1
            # print("Right: i, lo, hi", i, lo, hi)
            while lo + 1 < hi:
                mid = (lo + hi + 1) // 2
                if dp[mid + 1] - dp[i + 1] > value:
                    hi = mid
                else:
                    lo = mid
            ind = max(hi, ndr[i])
            # print("i, ind: ", i, ind)
            right_turns = ind - i

        ai = nm(left_turns, right_turns)
        if ai is not None:
            ans[i] = ai
    print(*ans)
