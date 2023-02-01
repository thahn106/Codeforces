for t in range(int(input())):
    n = int(input())
    s = set(list(map(int, input().split())))
    if len(s) == 2:
        print(n // 2 + 1)
    else:
        print(n)
