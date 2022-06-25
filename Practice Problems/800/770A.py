n,k = map(int, input().split())
ans = ""
for i in range(n):
    ans += chr((i%k)+ord('a'))
print(ans)
