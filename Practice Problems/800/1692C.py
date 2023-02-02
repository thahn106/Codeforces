def solve():
    input()
    grid = [input() for i in range(8)]
    for i in range(1, 7):
        for j in range(1, 7):
            if grid[i - 1][j - 1] == grid[i - 1][j + 1] == "#":
                print(i + 1, j + 1)
                return


for _ in range(int(input())):
    solve()
