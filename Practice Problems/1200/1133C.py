n = int(input())
a = sorted(list(map(int, input().split())))
j = 0
ans = 0
for i in range(n):
    cur = a[i]
    while j < n and a[j] < cur +6:
        j+=1
    ans = max(ans, j-i)
print(ans)