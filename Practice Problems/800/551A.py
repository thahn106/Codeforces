n = int(input())
a = list(map(int, input().split()))
s = {}
b = sorted(a, reverse=True)
for i, v in enumerate(b):
    if v not in s:
        s[v] = i+1

ans = [s[i] for i in a]
print(*ans)
