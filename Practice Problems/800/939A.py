n = int(input())
f = list(map(int,input().split()))

found = False
for i in range(n):
    if f[f[f[i]-1]-1]-1 == i:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
