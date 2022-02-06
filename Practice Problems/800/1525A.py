for _ in range(int(input())):
    k = int(input())
    e = 1
    t = 1
    while 100*e != t*k:
        if 100*e < t*k:
            e+=1
        t+=1
    print(t)
