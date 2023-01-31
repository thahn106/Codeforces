for t in range(int(input())):
    n, r, b = map(int, input().split())
    l, s = max(r, b), min(r, b)
    if r >= b:
        L = "R"
        S = "B"
    else:
        L = "B"
        S = "R"
    k = 1 + (l - 1) // (s + 1)
    sub = k * (s + 1) - l
    main = (s + 1) - sub
    assert sub * (k - 1) + main * k == l
    # print(main, sub, k)
    ans = [L * k] * main + [L * (k - 1)] * sub
    print(S.join(ans))
