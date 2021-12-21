n = int(input())
nums = list(map(int,input().split()))

ans = 0
start = 0
cur = 0
for i in range(n):
    if nums[i]>=cur:
        ans = max(ans, i-start+1)
    else:
        start = i
    cur = nums[i]
ans = max(n-start, ans)
print(ans)
