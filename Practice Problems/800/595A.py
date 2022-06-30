n, m = map(int, input().split())
a = 0
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(m):
        if l[2*j] or l[2*j+1]:
            a += 1
print(a)
