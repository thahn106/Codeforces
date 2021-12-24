n = int(input())
nums = list(map(int,input().split()))
m = max(nums)
ans = 0
for n in nums:
    ans += (m-n)
print(ans)
