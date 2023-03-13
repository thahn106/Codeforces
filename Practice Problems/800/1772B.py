for t in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    ma = max(a, b, c, d)
    mi = min(a, b, c, d)
    if (ma, mi) in [(a, d), (d, a), (b, c), (c, b)]:
        print("YES")
    else:
        print("NO")
