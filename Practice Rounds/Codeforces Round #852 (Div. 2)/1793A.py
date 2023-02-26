for _ in range(int(input())):
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    if b * (m + 1) < a * m:
        print(b * n)
    else:
        d = n // (m + 1)
        ans = d * a * m
        n -= d * (m + 1)
        ans += n * min(a, b)
        print(ans)
