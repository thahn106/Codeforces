for t in range(int(input())):
    ans = 1
    cur = 0
    s = set()
    for c in input():
        if c not in s:
            if cur < 3:
                cur += 1
                s.add(c)
            else:
                ans += 1
                cur = 1
                s = set()
                s.add(c)
    print(ans)