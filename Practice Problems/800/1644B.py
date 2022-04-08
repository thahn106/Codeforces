for t in range(int(input())):
    n = int(input())
    if n==3:
        print('3 2 1')
        print('3 1 2')
        print('1 3 2')
    else:
        for i in range(n):
            a = [(n-j+i)%n+1 for j in range(n)]
            print(*a)
