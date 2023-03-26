for t in range(int(input())):
    n, k = map(int, input().split())
    if n % 2:
        c = n // 2
        print(((k - 1) + (k - 1) // c) % n + 1)
    else:
        print((k - 1) % n + 1)
