for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = [(a[i],i) for i in range(n)]
    b.sort()
    if b[0][0]==b[-1][0]:
        print("NO")
        continue
    print("YES")
    hub = b[0][0]
    hl = b[0][1]+1
    m = b[-1][1]+1
    for i in range(1,n):
        if b[i][0] == hub:
            to = m
        else:
            to = hl
        print("{} {}".format(b[i][1]+1,to))
