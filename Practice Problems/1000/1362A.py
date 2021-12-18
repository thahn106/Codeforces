from math import ceil

for t in range(int(input())):
    a,b = map(int, input().split())
    ans = 0
    if a>b:
        while (a>b):
            b*=2
            ans +=1
    elif a<b:
        while (a<b):
            a*=2
            ans +=1
    if a==b:
        ans = ceil(ans/3)
    else:
        ans = -1
    print(ans)
