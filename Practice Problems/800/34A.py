n = int(input())
a = list(map(int,input().split()))
ans = -1
m = 1000
for i in range(n):
    d = abs(a[i]-a[(i+1)%n])
    if d < m:
        ans = i
        m = d

print(ans+1, ((ans+1)%n)+1)
