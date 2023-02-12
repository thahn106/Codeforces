for t in range(int(input())):
    n = int(input())
    if n == 3:
        print("NO")
    else:
        print("YES")
        if n % 2:
            d = n // 2
            ans = [-d if i % 2 else d - 1 for i in range(n)]
        else:
            ans = [1 - 2 * (i % 2) for i in range(n)]
        print(*ans)
