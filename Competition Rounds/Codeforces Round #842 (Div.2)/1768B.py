for t in range(int(input())):
    n,k = map(int, input().split())
    off = 0
    cur = 1
    for i in list(map(int, input().split())):
        if i == cur:
            cur +=1
        elif i>cur:
            off += 1
    q,r =  divmod(off,k)
    if r:
        q+=1
    print(q)