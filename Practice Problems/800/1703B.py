for t in range(int(input())):
    input()
    ans = 0
    so = set()
    s = input()
    for c in s:
        ans += 1
        if c not in so:
            ans += 1
            so.add(c)
    print(ans)