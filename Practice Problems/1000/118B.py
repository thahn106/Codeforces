n = int(input())
for i in range(2*n+1):
    k = abs(n-i)
    m = n-k
    row = " "*(2*k)
    for j in range(2*m+1):
        row+=str(m-abs(m-j))
        if j != 2*m:
            row+=" "
    print(row)
