N = int(input())
a = list(map(int, input().split()))
s = sum(a)
k, r = divmod(s,3)
if r:
    print(0)
else:
    dp = [0]*(N+1)
    run = 0
    two = 0
    for i,c in enumerate(a):
        run +=c
        dp[i+1] = run
        if run == 2*k and i != N-1:
            two += 1
    ans = 0
    for i in dp[1:-1]:
        if i == 2*k:
            two -= 1
        if i == k:
            ans += two
    print(ans)


    

