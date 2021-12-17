from math import ceil
n,m = map(int,input().split())
nums = list(map(int,input().split()))
ans = [(ceil(nums[i]/m), i+1) for i in range(n)]
ans.sort()
print(ans[-1][1])
