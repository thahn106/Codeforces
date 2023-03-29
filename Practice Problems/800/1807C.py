for t in range(int(input())):
    input()
    ref = {}
    pos = True
    for i, c in enumerate(input()):
        if c in ref:
            if ref[c] != i % 2:
                pos = False
                break
        else:
            ref[c] = i % 2
    if pos:
        print("YES")
    else:
        print("NO")
