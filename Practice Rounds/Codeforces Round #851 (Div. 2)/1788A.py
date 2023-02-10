for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    twos = sum(a) - n
    if twos % 2:
        print(-1)
    else:
        t = 0
        for i, c in enumerate(a):
            if c == 2:
                t += 1
            if 2 * t == twos:
                print(i + 1)
                break
