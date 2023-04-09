for t in range(int(input())):
    n = int(input())
    print(n)
    a = list(range(1, n + 1))
    for i in range(n):
        print(*a)
        a[0], a[n - 1 - i] = a[n - 1 - i], a[0]
