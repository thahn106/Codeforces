for t in range(int(input())):
    n, k  = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    ans = sum(nums[:n-2*k])
    mc =0
    count = 0
    cur=nums[-1]
    for i in range(2*k):
        if nums[n-1-i]==cur:
            count+=1
            mc = max(count, mc)
        else:
            count = 1
            cur = nums[n-1-i]
            mc = max(count, mc)
    ans += max(0, mc-k)
    print(ans)
