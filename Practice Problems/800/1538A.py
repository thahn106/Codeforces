for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ma = max(a)
    mi = min(a)
    ai = a.index(ma)
    ii = a.index(mi)
    print(min(max(ai+1,ii+1), max(n-ai,n-ii), (ai+1+n-ii), (ii+1+n-ai)))
