for t in range(int(input())):
    n = int(input())
    models = list(map(int,input().split()))
    dp = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        run = 1
        k = 2
        while k*(i+1) <= n:
            if models[k*(i+1)-1]>models[i]:
                run=max(run, dp[k*(i+1)-1]+1)
            k += 1
        dp[i]=run
    print(max(dp))
