import sys
import heapq

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lo = max(a) - 1
    hi = n * 10**9

    def check2(val):
        dp = [val] * (n + 1)
        start_idx = 0
        cur = 0
        dp[0] = 0
        minq = [(0, 0)]
        for i, x in enumerate(a):
            if x > val:
                return False
            while minq[0][1] < start_idx:
                heapq.heappop(minq)

            dp[i + 1] = x + minq[0][0]

            heapq.heappush(minq, (dp[i + 1], i + 1))
            cur += x
            while cur > val:
                cur -= a[start_idx]
                start_idx += 1
        while minq[0][1] < start_idx:
            heapq.heappop(minq)
        ans = minq[0][0]
        return ans <= val

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check2(mid):
            hi = mid
        else:
            lo = mid
    sys.stdout.write(str(hi) + "\n")
