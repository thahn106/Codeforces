n = int(input())
ans = 0
s = list(input())
for i in range(n//2):
    a = 2*i
    b = 2*i+1
    if s[a] == s[b]:
        ans += 1
        s[a] = 'a'
        s[b] = 'b'
print(ans)
print("".join(s))
