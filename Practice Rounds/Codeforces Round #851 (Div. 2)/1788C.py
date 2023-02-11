for t in range(int(input())):
    n = int(input())
    if n % 2:
        print("YES")
        d = (n - 1) // 2
        for i in range(1, d + 1):
            print(i, 3 * d + 2 + i)
        for i in range(d + 1, 2 * d + 2):
            print(i, d + 1 + i)
    else:
        print("NO")
