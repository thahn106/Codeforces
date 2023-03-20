for t in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    ans = 0
    for y in range(m):
        for x in range(n):
            cur = grid[x][y]
            for i in range(4):
                cx, cy = x, y
                cx += dx[i]
                cy += dy[i]
                while 0 <= cx < n and 0 <= cy < m:
                    cur += grid[cx][cy]
                    cx += dx[i]
                    cy += dy[i]
            ans = max(ans, cur)
    print(ans)
