from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for t in range(int(input())):
    n, m = map(int, input().split())
    matrix = [list(input()) for i in range(n)]

    def bc(y, x):
        return 0 <= y < n and 0 <= x < m

    empty_neighbors = [[0 for _ in range(m)] for i in range(n)]
    visited = [[False for _ in range(m)] for i in range(n)]
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == "L":
                start_point = (row, col)
                visited[row][col] = True
            for i in range(4):
                ny = row + dy[i]
                nx = col + dx[i]
                if bc(ny, nx) and matrix[ny][nx] != "#":
                    empty_neighbors[row][col] += 1

    remaining = deque()
    remaining.append(start_point)
    while len(remaining):
        row, col = remaining.popleft()
        for i in range(4):
            ny = row + dy[i]
            nx = col + dx[i]
            if not bc(ny, nx) or matrix[ny][nx] == "#" or visited[ny][nx]:
                continue
            empty_neighbors[ny][nx] -= 1
            if empty_neighbors[ny][nx] <= 1:
                visited[ny][nx] = True
                matrix[ny][nx] = "+"
                remaining.append((ny, nx))

    for row in matrix:
        sys.stdout.write(("".join(row)) + "\n")
