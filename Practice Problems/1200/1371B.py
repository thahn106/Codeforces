for t in range(int(input())):
    n,r = map(int,input().split())
    if r<n:
        ans = (r*(r+1))//2
    else:
        ans = (n*(n-1))//2 + 1
    print(ans)
