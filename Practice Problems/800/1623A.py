for t in range(int(input())):
    n,m,rb,cb,rd,cd = map(int,input().split())
    dr,dc = 1,1
    ans = 0
    while True:
        if rb == rd or cb == cd:
            print(ans)
            break
        if rb == 1 and dr == -1:
            dr = 1
        if rb == n and dr == 1:
            dr = -1
        if cb == 1 and dc == -1:
            dc = 1
        if cb == m and dc == 1:
            dc = -1
        rb += dr
        cb += dc
        ans +=1
