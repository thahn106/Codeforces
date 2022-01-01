k = int(input())
chars = [0 for i in range(26)]
for c in input():
    chars[ord(c)-97]+=1

possible = True
for c in chars:
    if c%k:
        possible = False

if possible:
    ans = ""
    for i in range(26):
        ans += chr(i+97)*(chars[i]//k)
    ans *= k
    print(ans)
else:
    print(-1)
