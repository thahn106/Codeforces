y, k, n = map(int, input().split())
ans = []
x = (-y) % k
while x <= n - y:
    if x:
        ans.append(x)
    x += k
if ans:
    print(*ans)
else:
    print(-1)
