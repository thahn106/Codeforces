N = int(input())
a = list(map(int, input().split()))

MOD = 10**9 + 7
pows = [1] * (N + 1)
cur = 1
for p in range(N):
    cur += cur
    if cur >= MOD:
        cur -= MOD
    pows[p + 1] = cur

ans = 0
for i in range(N - 1):
    it1 = i
    it2 = i
    for j in range(i + 1, N):
        while it1 >= 0 and 2 * a[i] - a[j] <= a[it1]:
            it1 -= 1
        while it2 < N and 2 * a[j] - a[i] > a[it2]:
            it2 += 1
        exp = (it1 + 1) + (N - it2)
        ans += pows[exp]
        if ans >= MOD:
            ans -= MOD
print(ans)
