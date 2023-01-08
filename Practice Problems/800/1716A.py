for t in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
    else:
        r, d = divmod(n, 3)
        print(r+bool(d))
