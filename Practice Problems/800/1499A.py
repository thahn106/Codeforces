for t in range(int(input())):
    n,k1,k2 = map(int,input().split())
    w,b = map(int,input().split())

    l = min(k1,k2)
    r = min(n-k1,n-k2)
    m = n-l-r
    if l+(m//2) >= w and r+(m//2) >= b:
        print("YES")
    else:
        print("NO")
