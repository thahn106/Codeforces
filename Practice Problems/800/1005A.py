n = int(input())
a = list(map(int,input().split()))
ans =[]
cur = 0
for i in a:
    if i<=cur:
        ans.append(cur)
    cur = i
ans.append(cur)
print(len(ans))
print(*ans)
