from math import ceil
for t in range(int(input())):
    a,b,c = map(int,input().split())
    if a>=c:
        first =-1
    else:
        first = 1
    if a*b<=c:
        second = -1
    else:
        second = b
    print("{} {}".format(first, second))
