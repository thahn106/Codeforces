for t in range(int(input())):
    a, K = map(int,input().split())
    i = 1
    while i < K:
        astr = [int(c) for c in str(a)]
        mi = min(astr)
        ma = max(astr)
        if mi == 0:
            i = K
        else:
            a += mi*ma
            i+=1
    print(a)
