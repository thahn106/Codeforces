from math import ceil

for t in range(int(input())):
    l,r,d = map(int,input().split())
    if d<l:
        print(d)
    else:
        R = r//d+1
        print(R*d)
