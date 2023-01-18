for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if len(a)>1:
        b = max(a[1:])-a[0]
        c = a[-1]-min(a[:-1])
        d = max([a[i]-a[(i+1)%n] for i in range(n)])
        print(max(b,c,d))
    else:
        print(0)
