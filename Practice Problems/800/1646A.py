for t in range(int(input())):
    n,s = map(int,input().split())
    ans,r = divmod(s,n**2)
    print(ans)
