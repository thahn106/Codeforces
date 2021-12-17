for q in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    start = -1
    count = 1
    for i in range(n):
        if nums[i] == nums[(i+1)%n]:
            start = (i+1)%n
        else:
            count = 2
    if count > 1:
        if start == -1 :
            start = 0
            if n%2==1:
                count = 3
        ans = [(((i-start)%n)%2)+1 for i in range(n)]
        if count == 3:
            ans[0]=3
    else:
        ans = [1 for i in range(n)]
    print(count)
    print(*ans)
