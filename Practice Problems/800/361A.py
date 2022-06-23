n, k = map(int, input().split())
for i in range(n):
    print(*[(int(i == j)*k)for j in range(n)])
