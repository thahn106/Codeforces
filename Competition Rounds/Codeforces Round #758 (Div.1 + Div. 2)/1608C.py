for t in range(int(input())):
    N = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    an = [(a[n], n) for n in range(N)]
    bn = [(b[n], n) for n in range(N)]


    an.sort()
    bn.sort()

    index_a = [0 for n in range(N)]
    index_b = [0 for n in range(N)]
    for n in range(N):
        index_a[an[n][1]]=n
        index_b[bn[n][1]]=n

    dpa = [N-1 for n in range(N)]
    dpb = [N-1 for n in range(N)]

    mina = N-1
    minb = N-1
    for n in range(N):
        ind = N-1-n
        mina = min(index_b[an[ind][1]],mina)
        dpa[ind]=mina
        minb = min(index_a[bn[ind][1]],minb)
        dpa[ind]=minb


    #two walks
    aline = N-1
    bline = N-1
    working=True
    while working:
        working = False
        if dpa[aline]<bline:
            bline = dpa[aline]
            working = True
        if dpa[bline]<aline:
            aline = dpa[bline]
            working = True

    ans = ["0" for n in range(N)]
    for n in range(N):
        if aline<=n:
            ans[an[n][1]]="1"
        if bline<=n:
            ans[bn[n][1]]="1"
    print("".join(ans))
