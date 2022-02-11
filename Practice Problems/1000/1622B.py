for t in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    s = list(map(int,list(input())))
    l = []
    d = []
    join = sorted(zip(p,list(range(n))))
    for r, i in join:
        if s[i]:
            l.append(i)
        else:
            d.append(i)
    q = d+l
    ratings = [0 for i in range(n)]
    for i in range(n):
        ratings[q[i]] = i+1
    print(*ratings)
