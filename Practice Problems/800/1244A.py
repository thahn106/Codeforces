from math import ceil
for t in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    P = ceil(a/c)
    p = ceil(b/d)
    if P+p <= k:
        print(P, p)
    else:
        print(-1)
