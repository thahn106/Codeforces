for t in range(int(input())):
    s = input()
    possible = True
    cur = '0'
    le = 0
    for c in s:
        if cur != c:
            if le == 1:
                possible = False
            cur = c
            le = 1
        else:
            le += 1
    if le == 1:
        possible = False
    if possible:
        print("YES")
    else:
        print("NO")
