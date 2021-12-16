n = int(input())
nums = list(map(int, input().split()))
nums.sort()
possible = False
for i in range(2,n):
    if nums[i]<nums[i-1]+nums[i-2]:
        possible = True
if possible:
    print("YES")
else:
    print("NO")
