for t in range(int(input())):
    n = int(input())
    taken = [False for i in range(n)]
    opt = True
    ps = [list(map(int,input().split())) for i in range(n)]
    for i in range(n):
        p = ps[i]
        found = False
        for k in p[1:]:
            if not taken[k-1]:
                taken[k-1]=True
                found = True
                break
        if opt and not found:
            opt = False
            princess = i
    if opt:
        print("OPTIMAL")
    if not opt:
        print("IMPROVE")
        for j in range(n):
            if not taken[j]:
                prince = j
                break
        print("{} {}".format(princess+1, prince+1))
