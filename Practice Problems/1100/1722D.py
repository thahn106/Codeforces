for t in range(int(input())):
    n = int(input())
    s = input()
    ref = 0
    dp = []
    for i, c in enumerate(s):
        left = i
        right = n - 1 - i
        if c == "L":
            cur, alt = left, right
        else:
            cur, alt = right, left
        ref += cur
        dp.append(max(0, alt - cur))
    dp.sort(reverse=True)
    ans = []
    for c in dp:
        ref += c
        ans.append(ref)
    print(*ans)
