def wall(char):
    if char == '#':
        return True
    else:
        return False

def main():
    n,m,k = [int(x) for x in input().split()]
    matrix = [[char for char in input()] for i in range(n)]

    visited = [[wall(char) for char in row] for row in matrix]

    for row in range(n):
        for col in range(m):
            if not visited[row][col]:
                start_point = (row,col)

    visits = []
    remaining = [start_point]
    while remaining:
        row, col = remaining.pop()
        visits.append((row,col))
        visited[row][col] = True
        if row>0:
            if not visited[row-1][col]:
                visited[row-1][col] = True
                remaining.append((row-1,col))
        if row < n-1:
            if not visited[row+1][col]:
                visited[row+1][col] = True
                remaining.append((row+1,col))
        if col>0:
            if not visited[row][col-1]:
                visited[row][col-1] = True
                remaining.append((row,col-1))
        if col<m-1:
            if not visited[row][col+1]:
                visited[row][col+1] = True
                remaining.append((row,col+1))

    fill = []
    if k>0:
        fill = visits[-k:]
    for point in fill:
        row,col = point
        matrix[row][col] = "X"
    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    main()
