from math import ceil
for t in range(int(input())):
    x,y,k = map(int, input().split())
    d,r = divmod(k*(y+1)-1,(x-1))
    print(k+d+(r>0))
