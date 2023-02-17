for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    k = [(c, i) for i, c in enumerate(s)]
    k.sort()
    ans = []
    for i, c in enumerate(s):
        if k[-1][1] == i:
            v = k[-2][0]
        else:
            v = k[-1][0]
        ans.append(c - v)
    print(*ans)
