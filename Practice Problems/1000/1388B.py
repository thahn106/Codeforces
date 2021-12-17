from math import ceil
for t in range(int(input())):
    n = int(input())
    r  = ceil(n/4)
    print("9"*(n-r)+"8"*r)
