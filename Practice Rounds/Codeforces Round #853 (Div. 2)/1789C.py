for t in range(int(input())):
    n, m = map(int, input().split())
    counts = [0] * (n + m + 1)
    a = list(map(int, input().split()))
    for x in a:
        counts[x] += m + 1
    for i in range(m):
        p, v = map(int, input().split())
        p -= 1
        counts[a[p]] -= m - i
        a[p] = v
        counts[a[p]] += m - i

    ans = 0
    for c in counts:
        ans += c * (m) - (c * (c - 1)) // 2
    print(ans)
