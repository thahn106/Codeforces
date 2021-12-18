MOD = 998244353

N = int(input())

def binom(n,k):
    if k> n/2:
        k = n-k
    ans = 1
    denom = 1
    for i in range(k):
        ans= ans*(n-i)%MOD
        denom= denom*(i+1)%MOD

    denom = pow(denom, -1, MOD)
    return ans*denom%MOD

B,W = 0,0

a = [[0 for i in range(3)] for j in range(3)]

for n in range(N):
    dom = input()
    if dom[0]=="B":
        B += 1
        i = 1
    elif dom[0]=="W":
        W += 1
        i = 2
    else:
        i = 0
    if dom[1]=="B":
        B += 1
        j = 1
    elif dom[1]=="W":
        W += 1
        j = 2
    else:
        j = 0
    a[i][j]+=1

if B>N or W>N:
    ans = 0
else:
    ans = binom(2*N-B-W,N-W)
    if a[1][1] == 0  and a[2][2] == 0:
        i = 0
        sub = 1
        while i < a[0][0]:
            sub = (sub*2)%MOD
            i+=1
        if a[1][0] == 0 and a[0][2] == 0 and a[1][2] == 0:
            sub -= 1
        if a[0][1] == 0 and a[2][0] == 0 and a[2][1] == 0:
            sub -= 1
        ans = (ans - sub)%MOD
print(ans)
