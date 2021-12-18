for t in range(int(input())):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    divs= {}
    for num in nums:
        div = (-1*num)%k
        if div != 0:
            if div not in divs:
                divs[div] =1
            else:
                divs[div] += 1
    ans = []
    for div in divs:
        ans.append((divs[div], div))
    ans.append((1,-1))
    ans.sort(reverse=True)
    a,b = ans[0]
    print((a-1)*k+b+1)
