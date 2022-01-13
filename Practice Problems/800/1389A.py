for t in range(int(input())):
    l,r = map(int,input().split())
    if r<2*l:
        print("-1 -1")
    else:
        print("{} {}".format(l, 2*l))
