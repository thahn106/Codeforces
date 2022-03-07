for q in range(int(input())):
    n,m = map(int,input().split())
    d = n//m
    m = m%10
    cycle = [m]
    cur = m
    while True:
        cur = (cur+m)%10
        if cur == cycle[0]:
            break
        else:
            cycle.append(cur)
    d,r = divmod(d, len(cycle))
    print(sum(cycle)*d+sum(cycle[:r]))
