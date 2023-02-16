MOD = 998244353

n = int(input())
w = list(map(int, input().split()))
k = n // 6

ans = 0
double = 0
trip = 0
for i in range(2 * k):
    a = [w[i * 3], w[i * 3 + 1], w[i * 3 + 2]]
    a.sort()
    if a[0] == a[2]:
        trip += 1
    elif a[0] == a[1]:
        double += 1

num = 1
den = 1
for i in range(k):
    num = (num * (2 * k - i)) % MOD
    den = (den * (i + 1)) % MOD

for i in range(double):
    num = (num * (2)) % MOD
for i in range(trip):
    num = (num * (3)) % MOD

ans = (num * pow(den, -1, MOD)) % MOD
print(ans)
