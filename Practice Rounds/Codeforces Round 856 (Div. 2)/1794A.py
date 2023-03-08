for t in range(int(input())):
    n = int(input())
    s = input().split()
    first = None
    second = None
    for c in s:
        if len(c) == n - 1:
            if first is None:
                first = c
            else:
                second = c
    if first[::-1] == second:
        print("YES")
    else:
        print("NO")
