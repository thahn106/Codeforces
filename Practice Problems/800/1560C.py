from math import sqrt, ceil
for t in range(int(input())):
    k = int(input())
    n = ceil(sqrt(k))
    d = n*n-k
    if d<n:
        print("{} {}".format(n,d+1))
    else:
        print("{} {}".format(2*n-d-1,n))
