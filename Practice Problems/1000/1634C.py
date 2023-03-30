for t in range(int(input())):
    n, k = map(int, input().split())
    if k == 1:
        print("YES")
        for i in range(n):
            print(i + 1)
        continue

    if n % 2 == 1:
        print("NO")
        continue

    print("YES")
    for i in range(n):
        print(*[x for x in range(i + 1, n * k + 1, n)])
