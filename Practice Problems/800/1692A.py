for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = int(b>a)+int(c>a)+int(d>a)
    print(ans)
