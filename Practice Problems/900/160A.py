n = int(input())
nums = list(map(int,input().split()))
s = sum(nums)
nums.sort(reverse=True)
ans = n
count = 0
run = 0
for num in nums:
    count +=1
    run += num
    if run > s-run:
        ans = min(count, ans)
print(ans)
