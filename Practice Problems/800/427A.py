n = int(input())
nums = [int(x) for x in input().split()]

ans = 0
run = 0
for num in nums:
    run -=num
    ans = max(ans, run)
print(ans)
