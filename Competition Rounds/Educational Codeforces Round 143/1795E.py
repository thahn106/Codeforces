import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dp = []

    val = 10**18
    for dir in range(2):
        dprun = [0] * n
        stack = []
        for i in range(n):
            while stack and stack[-1][0] > a[i] - i:
                stack.pop()
            j = max(-1, i - a[i])
            if stack:
                j = max(j, stack[-1][1])

            l = i - j
            dprun[i] = l * a[i] - (l * (l - 1) // 2)
            if j >= 0 and l < a[i]:
                dprun[i] += dprun[j]
            stack.append((a[i] - i, i))

        if dir:
            dprun.reverse()
        dp.append(dprun)
        a.reverse()

    ans = 10**12
    s = sum(a)
    for i, c in enumerate(a):
        cur = s - dp[0][i] - dp[1][i] + 2 * c
        ans = min(ans, cur)
    sys.stdout.write(str(ans) + "\n")
