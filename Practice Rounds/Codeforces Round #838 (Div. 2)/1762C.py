M = 998244353
for t in range(int(input())):
    n = int(input())
    ans = 1 
    cur = 1
    s = input()
    for i in range(1,n):
        if s[i] == s[i-1]:
            cur = (2*cur)%M
        else:
            cur = 1
        ans = (ans+cur)%M
    print(ans)
