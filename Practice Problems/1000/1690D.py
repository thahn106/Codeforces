for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = k
    cur = 0
    for i, c in enumerate(s):
        if c == "W":
            cur += 1
        if i >= k:
            if s[i - k] == "W":
                cur -= 1
        if i >= k - 1:
            ans = min(ans, cur)
    print(ans)
