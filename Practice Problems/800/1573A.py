for t in range(int(input())):
    n = int(input())
    s = list(map(int,list(input())))
    ans = 0
    for i,c in enumerate(s):
        if c:
            if i != n-1:
                ans += c+1
            else:
                ans += c
    print(ans)
