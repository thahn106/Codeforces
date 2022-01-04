colors= ["B","W"]
n,m = map(int,input().split())
board = []
unvisited = []
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] ==".":
            unvisited.append((i,j))
    board.append([c for c in row])

def dfs(a,b):
    to_visit = [(a,b,0)]
    while to_visit:
        i,j,c = to_visit.pop()
        if board[i][j] == ".":
            board[i][j]=colors[c]
            if i>0:
                to_visit.append((i-1,j,1-c))
            if i<n-1:
                to_visit.append((i+1,j,1-c))
            if j>0:
                to_visit.append((i,j-1,1-c))
            if j<m-1:
                to_visit.append((i,j+1,1-c))

for cell in unvisited:
    a,b = cell
    if board[a][b]==".":
        dfs(a,b)

for row in board:
    print("".join(row))
