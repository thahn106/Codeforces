for t in range(int(input())):
    n,m = map(int, input().split())
    N = n
    T = 0
    while not N%2:
        T +=1
        N = N//2
    N = n
    F = 0
    while not N%5:
        F +=1
        N = N//5
    ans = n*m
    cand = 1
    while True:
        if F>T:
            cand *= 2
            F -= 1
        elif T>F:
            cand *= 5
            T -=1
        else:
            cand *=10
        if m>=cand:
            ans = n*  (m//cand)*cand
        else:
            break
    print(ans)
    
