from math import ceil
for t in range(int(input())):
    a,b,n = map(int,input().split())
    a, b = min(a,b),max(a,b)
    ans = 0
    while b<=n:
        a,b = b,a+b
        ans +=1
    print(ans)
