for t in range(int(input())):
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort(reverse=True)
    ans = 0
    cur = 0
    for i in x:
        if cur < i:
            ans +=1
            cur += n-i
        else:
            break
    print(ans)
