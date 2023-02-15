for t in range(int(input())):
    n, k, b, s = map(int, input().split())
    d = s - b * k
    if d < 0 or d > n * (k - 1):
        print(-1)
    else:
        a = [0] * n
        a[0] = b * k
        i = 0
        while d:
            rem = min(d, k - 1)
            a[i] += rem
            d -= rem
            i += 1
        print(*a)
