n = int(input())
a = list(map(int,input().split()))

ans = 0
cur = 0
run = 0
for i in range(n):
    if a[i]>cur:
        run +=1
    else:
        run = 1
    ans = max(ans,run)
    cur = a[i]
print(ans)
