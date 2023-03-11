a = [0]
ans = 0
cur = 1
for i in range(9):
    for j in range(9 - i):
        ans += cur
        a.append(ans)
    cur *= 10
for t in range(int(input())):
    n = int(input())
    print(a[n])
