for t in range(int(input())):
    nums = list(map(int,input().split()))
    a = [nums[0], nums[1], nums[6]-nums[0]-nums[1]]
    print(*a)
