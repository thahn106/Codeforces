n, m = map(int, input().split())
b = [0]*m
for i in range(n):
    a = list(map(int, input().split()))
    for c in a[1:]:
        b[c-1] = 1
if sum(b) == m:
    print("YES")
else:
    print("NO")
