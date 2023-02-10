for t in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(n // 2, n // 2)
    else:
        a = ["", ""]
        i = 0
        for c in str(n):
            d, r = divmod(int(c), 2)
            if r:
                a[i] += str(d)
                a[1 - i] += str(d + 1)
                i = 1 - i
            else:
                a[0] += str(d)
                a[1] += str(d)
        print(int(a[0]), int(a[1]))
