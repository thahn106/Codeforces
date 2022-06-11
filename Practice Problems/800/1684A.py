for t in range(int(input())):
    n = list(map(int, list(input())))
    if len(n) == 2:
        print(n[1])
    else:
        print(min(n))
