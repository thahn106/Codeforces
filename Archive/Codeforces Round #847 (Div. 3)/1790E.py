for t in range(int(input())):
    x = int(input())
    a = x
    b = 0
    xb = bin(x)[2:]
    for ind, c in enumerate(xb):
        if c == "0":
            i = len(xb) - 1 - ind
            if 2 * x - a - b >= 2 ** (i + 1):
                a += 2**i
                b += 2**i
    if a + b == 2 * x and a ^ b == x:
        print(a, b)
    else:
        print(-1)
