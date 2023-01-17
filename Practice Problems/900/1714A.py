for _ in range(int(input())):
    n,H,M = map(int, input().split())
    
    ans = 24*60
    for i in range(n):
        h,m = map(int, input().split())
        t = ((h-H)*60+m-M)%(24*60)
        ans = min(ans,t)
    h,m = divmod(ans,60)
    print(h,m)