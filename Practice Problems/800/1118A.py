for q in range(int(input())):
    n, a, b = map(int, input().split())
    d, r = divmod(n, 2)
    if 2*a<=b:
        print(n*a)
    else:
        print(d*b+r*a)
