for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a*d == b*c:
        print(0)
    elif a == 0 or c == 0 or (a*d) % (b*c) == 0 or (b*c) % (a*d) == 0:
        print(1)
    else:
        print(2)
