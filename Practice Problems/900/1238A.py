from math import gcd
for t in range(int(input())):
    x,y = map(int,input().split())
    if x-y>1:
        print("YES")
    else:
        print("NO")
