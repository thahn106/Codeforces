for t in range(int(input())):
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        row = list(map(int,input().split()))
        grid.append(row)

    possible = True
    mg = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i == 0 or i == n-1) and (j == 0 or j == m-1):
                ng = 2
            elif (i == 0 or i == n-1) or (j == 0 or j == m-1):
                ng = 3
            else:
                ng = 4
            row.append(ng)
            if grid[i][j]>ng:
                possible = False
        mg.append(row)
    if possible:
        print("YES")
        for row in mg:
            print(*row)
    else:
        print("NO")
