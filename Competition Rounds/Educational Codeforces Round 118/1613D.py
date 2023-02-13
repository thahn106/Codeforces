MOD = 998244353

for t in range(int(input())):
    n = int(input())
    dp1 = [0] * +(n + 2)
    dp2 = [0] * +(n + 2)
    dp1[0] = 1
    num_list = list(map(int, input().split()))
    for x in num_list:
        dp1[x + 1] = (2 * dp1[x + 1] + dp1[x]) % MOD
        if x:
            dp2[x - 1] = (2 * dp2[x - 1] + dp1[x - 1]) % MOD
        dp2[x + 1] = (2 * dp2[x + 1]) % MOD
    print((sum(dp1) + sum(dp2) - 1) % MOD)
