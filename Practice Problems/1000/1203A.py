for q in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    cc = True
    c = True
    for i in range(1,n):
        d = (p[i]-p[i-1])%n
        if d != 1:
            c = False
        if d != n-1:
            cc = False
    if c or cc:
        print("YES")
    else:
        print("NO")
