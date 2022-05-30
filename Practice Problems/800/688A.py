n,d = map(int,input().split())
r = '1'*n
ans = 0
cur = 0
for i in range(d):
    if input() == r:
        cur = 0
    else:
        cur += 1
    ans = max(ans,cur)
print(ans)
