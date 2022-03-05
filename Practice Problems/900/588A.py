ans = 0
m = 100
for n in range(int(input())):
    a, p = map(int, input().split())
    m = min(m, p)
    ans += a*m
print(ans)
