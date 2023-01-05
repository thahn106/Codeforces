for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ofc = [0]*n
    cycles = []
    cur = 1
    for i,c in enumerate(a):
        if not(c-1 == i or ofc[i]):
            ofc[i]=cur
            j = c-1
            cycle = 1
            while j != i:
                ofc[j] = cur
                j = a[j]-1
                cycle += 1
            cur +=1
            cycles.append(cycle)

    pair = False
    for i in range(1,n):
        if ofc[i] and ofc[i]==ofc[i-1]:
            pair = True
    if not cycles:
        print(1)
    else:
        ans = sum(cycles)-len(cycles)+1
        if pair: ans -=2
        print(ans)