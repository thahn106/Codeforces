import sys

input = sys.stdin.readline


for t in range(int(input())):
    n, X = map(int, input().split())
    a = list(map(int, input().split()))
    a = [k - 1 for k in a]

    dp = {}

    # dp[(l,r,x)]is number of moves neede to make a[l:r+1] all x
    def solve(l, r, x):
        if l > r:
            return 0
        if l == r:
            if a[l] == x:
                return 0
            return 1

        if (l, r, x) in dp:
            return dp[(l, r, x)]

        if a[l] == x:
            ans = solve(l + 1, r, x)
            for dif_x in range(X):
                if dif_x == x:
                    continue
                ans = min(ans, 1 + solve(l + 1, r, dif_x))
            dp[(l, r, x)] = ans
            return ans

        if a[r] == x:
            ans = solve(l, r - 1, x)
            for dif_x in range(X):
                if dif_x == x:
                    continue
                ans = min(ans, 1 + solve(l, r - 1, dif_x))
            dp[(l, r, x)] = ans
            return ans

        first_x = -1
        for i in range(l, r + 1):
            if a[i] == x:
                if first_x == -1:
                    first_x = i
                last_x = i

        # no x
        if first_x == -1:
            dp[(l, r, x)] = 1
            return 1

        # one x
        if first_x == last_x:
            dp[(l, r, x)] = 2
            return 2

        ans = 2 + solve(first_x, last_x, x)

        for dif_x in range(X):
            if dif_x == x:
                continue
            ans = min(ans, 1 + solve(first_x, last_x, dif_x))
        dp[(l, r, x)] = ans
        return ans

    ans = n - 1
    for x in range(X):
        ans = min(ans, solve(0, n - 1, x))
    print(ans)
