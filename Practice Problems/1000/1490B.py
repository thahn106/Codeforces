for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    c = [0,0,0]
    for num in nums:
        c[num%3]+=1

    ans = 0
    k = n//3
    while max(c)*3 != n:
        if c[0]>k:
            ans += c[0]-k
            c[0],c[1] = k, c[1]+c[0]-k
        if c[1]>k:
            ans += c[1]-k
            c[1],c[2] = k, c[2]+c[1]-k
        if c[2]>k:
            ans += c[2]-k
            c[2],c[0] = k, c[0]+c[2]-k
    print(ans)
