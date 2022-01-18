s = input()
k = int(input())
w = list(map(int,input().split()))
m = max(w)
ans = 0
for i in range(len(s)):
    ans += w[ord(s[i])-97]*(i+1)
for i in range(len(s),len(s)+k):
    ans += m*(i+1)
print(ans)
