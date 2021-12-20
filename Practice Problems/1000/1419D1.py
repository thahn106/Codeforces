n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = [0 for i in range(n)]

i = 1
count = 0
if n==1:
    print(0)
    print(*nums)
else:
    while count<n:
        ans[i]=nums[count]
        i+=2
        if i>=n:
            i=0
        count+=1
    print((n-1)//2)
    print(*ans)
