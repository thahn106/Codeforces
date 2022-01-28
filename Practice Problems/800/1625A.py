for t in range(int(input())):
    n,l = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 0
    for i in range(l):
        o =0
        for j in range(n):
            if x[j]%2:
                o+=1
            x[j] = x[j]//2
        if o > n//2:
            ans += 2**i
    print(ans)
