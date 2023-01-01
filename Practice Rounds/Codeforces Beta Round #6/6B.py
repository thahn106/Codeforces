n, m, c = input().split()
N,M = int(n),int(m)
grid = [input() for n in range(N)]

cols = [0]*26

def check(i,j):
    global c
    if (0<=i<N) and (0<=j<M):
        cell = grid[i][j]
        if cell !=c and cell != '.':
            cols[ord(cell)-ord('A')]=1


for i in range(N):
    for j in range(M):
        if grid[i][j] == c:
            check(i+1,j)
            check(i-1,j)
            check(i,j+1)
            check(i,j-1)

print(sum(cols))