n = int(input())
a = list(map(int, input().split()))
ans = n
mi = min(a)
ma = max(a)

for i in a:
    if i == mi or i == ma:
        ans -= 1
print(ans)
