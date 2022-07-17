s = input()
M = sorted(list(s))[-1]
ans = ""
for c in s:
    if c == M:
        ans += M
print(ans)
