for t in range(int(input())):
    n = int(input())
    a = [i + 2 for i in range(n)]
    a[-1] = 2
    a[0] = 1
    print(*a)
