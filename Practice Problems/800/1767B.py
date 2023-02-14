for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a[1:])
    a = a[0]
    for i in b:
        if i > a:
            d = i - a
            a += (d + 1) // 2
    print(a)
