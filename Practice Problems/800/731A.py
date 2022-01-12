s = input()
ans = 0
p = 0
for t in s:
    c = ord(t)-97
    ans += min((26+p-c)%26,(26+c-p)%26)
    p = c
print(ans)
