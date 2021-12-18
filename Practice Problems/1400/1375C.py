for t in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    pivots = [nums[0]]
    for num in nums:
        p = pivots[-1]
        if num < p:
            pivots.append(num)
    if nums[-1] >= max(pivots):
        print("YES")
    else:
        print("NO")
