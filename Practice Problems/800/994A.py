n, m = map(int, input().split())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = []
for i in x:
    if i in y:
        ans.append(i)
print(*ans)
