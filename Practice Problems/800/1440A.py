for t in range(int(input())):
    n,c0,c1,h = map(int,input().split())
    s = input()
    ans = 0
    C0 = min(c0, c1+h)
    C1 = min(c1, c0+h)
    for c in s:
        if c == '0':
            ans += C0
        else:
            ans += C1
    print(ans)
