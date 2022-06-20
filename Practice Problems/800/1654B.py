for t in range(int(input())):
    s = input()
    t = set()
    ans = 0
    for i, c in enumerate(s[::-1]):
        if c not in t:
            ans = i
            t.add(c)
    print(s[-(ans+1):])
