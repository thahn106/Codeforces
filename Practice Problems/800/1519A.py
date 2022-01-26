from math import ceil
for t in range(int(input())):
    r,b,d = map(int,input().split())
    if ceil((max(r,b)-min(r,b))/min(r,b)) <=d:
        print("YES")
    else:
        print("NO")
