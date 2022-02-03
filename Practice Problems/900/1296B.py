for t in range(int(input())):
    s = int(input())
    ans = 0
    while s:
        d,s = divmod(s,10)
        if d:
            ans += 10*d
            s += d
        else:
            ans += s
            s = 0
    print(ans)
