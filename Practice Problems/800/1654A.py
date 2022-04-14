for t in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(sum(a[-2:]))
