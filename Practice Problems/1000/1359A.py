import math
for t in range(int(input())):
    n,m,k = [int(x) for x in input().split()]
    x = min(n//k,m)
    print(x-math.ceil((m-x)/(k-1)))
