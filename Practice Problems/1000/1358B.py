for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = 1
    for i in range(n):
        if nums[i] <= i+1:
            ans = i+2
    print(ans)
