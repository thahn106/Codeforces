for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    e, o = 0, 0
    for c in a:
        if c % 2:
            o += c
        else:
            e += c
    if e > o:
        print("YES")
    else:
        print("NO")
