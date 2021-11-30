MOD = 1000000007

def main():
    N,K,D = [int(x) for x in input().split()]
    # dp
    paths = [1]
    for i in range(1, N+1):
        run = 0
        for j in range(max(0,i-K),i):
            run = (run+paths[j])%MOD
        paths.append(run)
    # print(paths)
    dp = []
    for n in range(N+1):
        if n < D:
            dp.append(0)
        else:
            sub = 0
            for j in range(1,min(n+1,K+1)):
                if j >= D:
                    sub = (sub+paths[n-j])%MOD
                else:
                    sub = (sub+dp[n-j])%MOD
            dp.append(sub)
    # print(dp)
    print(dp[N])





if __name__ == "__main__":
    main()
