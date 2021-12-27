n = int(input())
nums = list(map(int,input().split()))
a = [0,0]
i=0
h = 0
t = n-1
while h<=t:
    if nums[h]<nums[t]:
        a[i]+=nums[t]
        t-=1
    else:
        a[i]+=nums[h]
        h+=1
    i=1-i
print(*a)
