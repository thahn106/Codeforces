for t in range(int(input())):
    x,y,n = map(int,input().split())
    ans = x*(n//x) +y
    if ans > n:
        ans -= x
    print(ans)
