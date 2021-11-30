def divs(N,K):
    div = 0
    if N==0:
        return -1
    while (N%K==0):
        div += 1
        N /= K
    return div

def path(matrix, n, k):
    factor_matrix = []
    cand = False
    for i in range(n):
        row = []
        for j in range(n):
            val = divs(matrix[i][j],k)
            if val == -1:
                cand = (1, ("D"*i)+("R"*(n-1))+("D"*(n-1-i)))
                val = 0
            row.append(val)
        factor_matrix.append(row)

    path_matrix = [[0 for x in row]  for row in matrix]
    for i in range(1,n):
        factor_matrix[i][0]+=factor_matrix[i-1][0]
        path_matrix[i][0]=1
        factor_matrix[0][i]+=factor_matrix[0][i-1]
    for row in range(1,n):
        for col in range(1,n):
            if factor_matrix[row-1][col]<factor_matrix[row][col-1]:
                factor_matrix[row][col]+=factor_matrix[row-1][col]
                path_matrix[row][col]=1
            else:
                factor_matrix[row][col]+=factor_matrix[row][col-1]
    path = ""
    row, col = n-1, n-1
    while row+col>0:
        if path_matrix[row][col] == 1:
            path+="D"
            row -=1
        else:
            path+="R"
            col-=1
    if factor_matrix[n-1][n-1]>1 and cand:
        return cand
    return factor_matrix[n-1][n-1], path[::-1]

def main():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    v2, p2 = path(matrix, n, 2)
    v5, p5 = path(matrix, n ,5)
    if v2<v5:
        print(v2)
        print(p2)
    else:
        print(v5)
        print(p5)


if __name__ == "__main__":
    main()
