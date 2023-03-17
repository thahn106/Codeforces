for t in range(int(input())):
    n, m = map(int, input().split())
    ans = ["B"] * m
    a = list(map(int, input().split()))
    for c in a:
        small = min(c - 1, m - c)
        large = m - 1 - small
        if ans[small] == "A":
            ans[large] = "A"
        else:
            ans[small] = "A"
    print("".join(ans))
