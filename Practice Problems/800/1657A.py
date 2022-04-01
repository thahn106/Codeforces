from math import isqrt
for t in range(int(input())):
    x,y = map(int,input().split())
    d = x*x+y*y
    if not d:
        print(0)
    elif isqrt(d)**2==d:
        print(1)
    else:
        print(2)
