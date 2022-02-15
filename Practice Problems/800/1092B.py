n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
for i in range(n//2):
    ans += max(a[2*i:2*i+2])- min(a[2*i:2*i+2])
print(ans)
