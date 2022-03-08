n = int(input())
for i in range(n):
    row = []
    for j in range(n):
        d = (i+j)%n +1
        row.append(j*n+d)
    print(*row)
