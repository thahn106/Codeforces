n, k = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0
walks = [nums[0]]
for num in nums[1:]:
    ans += max(k-walks[-1], num)-num
    walks.append(max(k-walks[-1], num))
print(ans)
print(*walks)
