n,k = map(int,input().split())
s = input()
chars = input().split()

char = [False for i in range(26)]
for c in chars:
    char[ord(c)-97]=True

ss = []
start = -1
for i in range(n):
    c = s[i]
    if char[ord(c)-97]:
        if start == -1:
            start = i
    else:
        if start != -1:
            ss.append(i-start)
            start = -1
if start != -1:
    ss.append(n-start)

ans = 0
for s in ss:
    ans += (s*(s+1))//2
print(ans)
