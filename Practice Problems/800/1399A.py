for t in range(int(input())):
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    possible = True
    for i in range(n-1):
        if nums[i+1]-nums[i]>1:
            possible= False
    if possible:
        print("YES")
    else:
        print("NO")
