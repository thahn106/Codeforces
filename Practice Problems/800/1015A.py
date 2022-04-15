n, m = map(int, input().split())
ans = [1]*m
for i in range(n):
    l, r = map(int, input().split())
    for k in range(l, r+1):
        ans[k-1] = 0
print(sum(ans))
al = []
for i in range(m):
    if ans[i]:
        al.append(i+1)
print(*al)
