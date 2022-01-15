n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
for i,n in enumerate(a):
    ans += abs(i+1-n)
print(ans)
