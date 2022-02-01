for t in range(int(input())):
    n = int(input())
    first = True
    grid = []
    for i in range(n):
        row = [c for c in input()]
        grid.append(row)
        for j in range(n):
            if row[j]=='*':
                if first:
                    x1,y1 = i,j
                    first = False
                else:
                    x2,y2 = i,j
    if x1==x2:
        x3 = (x1+1)%n
        grid[x3][y1]='*'
        grid[x3][y2]='*'
    elif y1==y2:
        y3 = (y1+1)%n
        grid[x1][y3]='*'
        grid[x2][y3]='*'
    else:
        grid[x1][y2]='*'
        grid[x2][y1]='*'
    for row in grid:
        print("".join(row))
