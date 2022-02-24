n = int(input())
a = list(map(int,input().split()))
ans = []
s = {}
for i in a[::-1]:
    if i not in s:
        ans.append(i)
        s[i] = True
ans.reverse()
print(len(ans))
print(*ans)
