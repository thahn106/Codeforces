for t in range(int(input())):
    n = int(input())
    print(2)
    ans = []
    for i in range(1, n+1, 2):
        cur = i
        while cur <= n:
            ans.append(cur)
            cur *= 2
    print(*ans)
