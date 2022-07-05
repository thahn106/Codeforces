for t in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    if l2<=l1<=r2:
        print(l1)
    elif l1<=l2<=r1:
        print(l2)
    else:
        print(l1+l2)
