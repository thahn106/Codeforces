for t in range(int(input())):
    n = int(input())
    count = [0]*101
    for c in input().split():
        count[int(c)] += 1
    A = 0
    B = 0
    bfound = False
    for i,c in enumerate(count):
        if c>=2:
            continue
        elif c == 1:
            if not bfound:
                bfound = True
                B = i
        else:
            if not bfound:
                B = i
            A = i
            break
    print(A+B)
