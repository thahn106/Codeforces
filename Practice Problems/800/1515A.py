for t in range(int(input())):
    n, x = map(int,input().split())
    w = list(map(int,input().split()))
    w.sort()
    run = 0
    possible = True
    for i,n in enumerate(w):
        if run + n == x:
            if w[-1] == n:
                possible = False
            else:
                w[i] = w[-1]
                w[-1]= n
            break
        else:
            run += n
    if possible:
        print("YES")
        print(*w)
    else:
        print("NO")
