for t in range(int(input())):
    n, s, r = map(int, input().split())
    a = [1] * n
    m = s - r
    a[0] = m
    r -= n - 1
    for i in range(1, n):
        if r:
            d = min(r, m - 1)
            a[i] += d
            r -= d
        else:
            break
    print(*a)
