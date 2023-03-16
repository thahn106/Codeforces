for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    cur = 0
    ans = []
    for start, end in zip(s, f):
        cur = max(cur, start)
        ans.append(end - cur)
        cur = end
    print(*ans)
