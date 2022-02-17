from math import ceil
for t in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    mi = ceil(sum(a)/x)
    ma = 0
    for i in a:
        ma += ceil(i/x)
    print(mi,ma)
