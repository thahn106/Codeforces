from math import gcd
for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in a:
        if i%2:
            c.append(i)
        else:
            b.append(i)
    a = b+c
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if gcd(a[i],2*a[j])>1:
                ans +=1
    print(ans)
