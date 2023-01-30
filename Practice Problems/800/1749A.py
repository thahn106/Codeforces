for t in range(int(input())):
    n, m = map(int, input().split())
    x = set()
    y = set()
    for _ in range(m):
        a, b = map(int, input().split())
        x.add(a)
        y.add(b)
    xs = n - len(x)
    ys = n - len(y)
    xl = m - len(x)
    yl = m - len(y)
    if m > n:
        print("NO")
    else:
        if (xs and yl == 0 and xl <= 1) or (ys and xl == 0 and yl <= 1):
            print("YES")
        else:
            print("NO")
