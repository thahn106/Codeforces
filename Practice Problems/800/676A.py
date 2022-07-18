n = int(input())
a = list(map(int, input().split()))
ans = 1
for i in range(n):
    if a[i] == 1 or a[i] == n:
        ans = max(ans, i, n-i-1)
print(ans)
