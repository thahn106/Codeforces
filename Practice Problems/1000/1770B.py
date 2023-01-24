for t in range(int(input())):
    n, k = map(int, input().split())
    ans = [((i + 1) // 2 if i % 2 else n - i // 2) for i in range(n)]
    print(*ans)
