MOD = 10**9+7
for t in range(int(input())):
    n,k = map(int,input().split())
    ans = 1
    for i in range(k):
        ans = (ans*n)%MOD
    print(ans)
