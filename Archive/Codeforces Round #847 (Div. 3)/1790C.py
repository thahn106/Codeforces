for t in range(int(input())):
    n = int(input())
    c = [0] * n
    grid = [list(map(int, input().split())) for _ in range(n)]
    for row in grid:
        c[row[0] - 1] += 1
    for i, k in enumerate(c):
        if k == n - 1:
            ans = [i + 1]
    for row in grid:
        if row[0] != ans[0]:
            ans += row
            break
    print(*ans)
