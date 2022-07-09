n = int(input())
p = list(map(int,input().split()))
m = max(p)
s = sorted(p)[-2]
ans = 0
for i, c in enumerate(p):
    if c == m:
        ans = i+1
print(ans, s)
