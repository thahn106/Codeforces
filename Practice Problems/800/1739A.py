for t in range(int(input())):
    x, y = map(int, input().split())
    if x < 2 or y < 2:
        print(1, 1)
    else:
        print(2, 2)
