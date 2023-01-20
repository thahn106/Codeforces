for t in range(int(input())):
    m,n = map(int, input().split())
    ans = (n*(n+1)//2)
    if m > 1:
        ans += n*(m*(m+1))//2-n
    print(ans) 