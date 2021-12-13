nums = [int(x) for x in input().split()]
nums.sort()
a,b,c,d = nums
print("{} {} {}".format(d-c,d-b,d-a))
