import math
for t in range(int(input())):
    n = int(input())
    nums  = list(map(int, input().split()))
    possible = True
    s = 2*sum(nums)/((n)*(n+1))
    if s==math.floor(s):
        s = int(s)
        a = []
        for i in range(n):
            temp =  (nums[(i-1)%n]-nums[i]+s)/n
            if temp == math.floor(temp) and temp>0:
                a.append(int(temp))
            else:
                possible = False
    else:
        possible=False
    if possible:
        print("YES")
        print(*a)
    else:
        print("NO")
