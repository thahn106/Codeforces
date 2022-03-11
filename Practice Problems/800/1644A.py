for t in range(int(input())):
    r,g,b = [False]*3
    working = True
    for c in input():
        if c == 'r': r = True
        elif c == 'g': g = True
        elif c == 'b': b = True
        elif c == "R":
            if not r:
                working = False
                break
        elif c == "G":
            if not g:
                working = False
                break
        elif c == "B":
            if not b:
                working = False
                break

    if working: print("YES")
    else: print("NO")
