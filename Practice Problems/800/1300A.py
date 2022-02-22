for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in a:
        if i==0:
            ans +=1
    s = sum(a)+ans
    if s == 0:
        ans+=1
    print(ans)
