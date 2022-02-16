from math import ceil
for t in range(int(input())):
    a,b,c,d = map(int,input().split())
    ans = 0
    ans += b
    a -= b
    if a>0:
        if c<=d:
            print(-1)
            continue
        else:
            k = ceil(a/(c-d))
            ans += k*c
    print(ans)
