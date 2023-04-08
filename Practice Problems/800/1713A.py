for t in range(int(input())):
    n = int(input())
    mx, nx, my, ny = 0, 0, 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        mx = max(mx, x)
        my = max(my, y)
        nx = min(nx, x)
        ny = min(ny, y)
    nx = abs(nx)
    ny = abs(ny)
    print(2 * (mx + nx + my + ny))
