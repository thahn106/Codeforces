for t in range(int(input())):
    n,m = map(int,input().split())
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i+j)%2==0:
                row.append('B')
            else:
                row.append('W')
        matrix.append(row)
    if n*m %2==0:
        matrix[0][1]='B'
    for row in matrix:
        print("".join(row))
