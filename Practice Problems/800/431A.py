a = list(map(int,input().split()))
s = input()
ans = 0
for c in s:
    ans+=a[int(c)-1]
print(ans)
