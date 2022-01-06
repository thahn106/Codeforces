n = int(input())
p = list(map(int,input().split()))
s = sum(p)
q,r = divmod(n,s)
if r == 0:
    r += s
ans = 7
for i,d in enumerate(p):
    if r<=d:
        ans= min(ans, i+1)
    else:
        r -= d
print(ans)
