n,k = map(int,input().split())
a = list(map(int,input().split()))

start = 0
end = n-1
ans = 0

while start<n and a[start] <=k:
    ans +=1
    start +=1
if start <n:
    while end>=0 and a[end] <=k:
        ans +=1
        end-=1
print(ans)
