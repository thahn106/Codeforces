for t in range(int(input())):
    n = int(input())
    o = []
    e = []
    for i in list(map(int,input().split())):
        if i%2:
            o.append(i)
        else:
            e.append(i)
    a = o+e
    print(*a)
