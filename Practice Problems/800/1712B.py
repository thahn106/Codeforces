for t in range(int(input())):
    n = int(input())
    if n % 2:
        a = [1] + [i + 3 - 2 * (i % 2) for i in range(n - 1)]
    else:
        a = [i + 2 - 2 * (i % 2) for i in range(n)]
    print(*a)
