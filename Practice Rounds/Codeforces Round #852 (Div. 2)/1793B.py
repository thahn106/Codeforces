for t in range(int(input())):
    x, y = map(int, input().split())

    n = 2 * (x - y)
    ans = list(range(y, x)) + list(range(x, y, -1))
    print(n)
    print(*ans)
