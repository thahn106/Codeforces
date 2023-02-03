for t in range(int(input())):
    n = int(input())
    if n == 3:
        print(-1)
    elif n == 7:
        print("6 7 4 5 3 2 1")
    elif n == 9:
        print("6 7 8 9 3 2 1 4 5")
    elif n % 2:
        ans = [i + 6 for i in range(n - 5)] + [5, 4, 1, 2, 3]
        print(*ans)
    else:
        ans = [2 * ((i + 2) // 2) - (i % 2) for i in range(n)]
        print(*ans)
