for t in range(int(input())):
    k, n = map(int, input().split())
    cur = 1
    dif = 0
    ans = []
    for i in range(k):
        if cur + dif + k - 1 - i <= n:
            cur += dif
            dif += 1
        else:
            cur += 1
        ans.append(cur)
    print(*ans)
