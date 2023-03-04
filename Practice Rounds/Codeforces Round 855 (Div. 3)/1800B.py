for t in range(int(input())):
    n, k = map(int, input().split())
    uc = [0] * 26
    lc = [0] * 26
    for c in input():
        if c.isupper():
            uc[ord(c) - 65] += 1
        else:
            lc[ord(c) - 97] += 1

    ans = 0
    for a, b in zip(uc, lc):
        a, b = min(a, b), max(a, b)
        dif = b - a
        ans += a
        d = min(dif // 2, k)
        k -= d
        ans += d
    print(ans)
