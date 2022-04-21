for t in range(int(input())):
    l, r, a = map(int, input().split())
    q, d = divmod(r, a)
    q2, d2 = divmod(l, a)
    if q2 < q:
        print(max(q+d, q+a-2))
    else:
        print(q+d)
