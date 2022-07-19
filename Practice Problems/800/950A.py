l, r, a = map(int, input().split())
ans = min(l,r)
t = max(l,r)-min(l,r)
if t <= a:
    ans += (a+t)//2
else:
    ans += a
print(2*ans)
