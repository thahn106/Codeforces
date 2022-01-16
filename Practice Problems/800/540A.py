n = int(input())
s = input()
t = input()
ans = 0
for a,b in zip(s,t):
    a = int(a)
    b = int(b)
    t = abs(a-b)
    ans += min(t,10-t)
print(ans)
