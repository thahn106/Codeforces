for t in range(int(input())):
    n,m,r,c = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(input())
    if grid[r-1][c-1]=='B':
        print(0)
    else:
        adj = False
        found = False
        for i,row in enumerate(grid):
            if not found:
                if 'B' in row:
                    found = True
            if row[c-1]=='B':
                adj = True
            if i == r-1:
                if 'B' in row:
                    adj = True
        if not found:
            print(-1)
        else:
            if adj:
                print(1)
            else:
                print(2)
