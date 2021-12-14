for t in range(int(input())):
    n = int(input())
    if n == 2:
        print(-1)
    else:
        for i in range(n):
            row = []
            for j in range(n):
                row.append(n*((j-i)%n)+(j+1))
            print(*row)
