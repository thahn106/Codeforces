n, a = map(int,input().split())
t = list(map(int,input().split()))
dis = [0 for i in range(100)]
count = [0 for i in range(100)]

for i in range(n):
    dis[abs(a-1-i)] += 1
    if t[i]:
        count[abs(a-1-i)]+=1
ans = 0
for i in range(n):
    if dis[i]==count[i]:
        ans += count[i]
print(ans)
