for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odds = []
    evens = []
    for i, c in enumerate(a):
        if c % 2:
            odds.append(i + 1)
        else:
            evens.append(i + 1)
    if len(odds) >= 1 and len(evens) >= 2:
        print("YES")
        print(odds[0], evens[0], evens[1])
    elif len(odds) >= 3:
        print("YES")
        print(*odds[:3])
    else:
        print("NO")
