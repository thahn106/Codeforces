n, m = map(int, input().split())
ans = 100
for i in range(n):
    a, b = map(int, input().split())
    ans = min(ans, a/b)
print(ans*m)
