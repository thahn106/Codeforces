for t in range(int(input())):
    n, m, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pos = [0] * (n + 1)
    for i, c in enumerate(a):
        pos[c] = i + 1
    ans = 2 * n

    for i in range(1, m):
        x, y = b[i - 1], b[i]
        if pos[y] < pos[x] or pos[y] > pos[x] + d:
            ans = 0
        else:
            ans = min(ans, pos[y] - pos[x])
            if d + 1 <= n - 1:
                ans = min(ans, d - (pos[y] - pos[x] - 1))
    print(ans)
