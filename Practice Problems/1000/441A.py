n,v = map(int,input().split())
ans = []
for i in range(n):
    p = list(map(int,input().split()))[1:]
    if min(p)<v:
        ans.append(i+1)

print(len(ans))
print(*ans)
