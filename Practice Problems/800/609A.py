n = int(input())
m = int(input())
a = [int(input()) for i in range(n)]
a.sort(reverse=True)
ans = 0
for i in range(n):
    ans += a[i]
    if ans >= m:
        print(i+1)
        break
