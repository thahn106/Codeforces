for t in range(int(input())):
    w,h,n = map(int,input().split())
    ans = 1
    while not w%2:
        w=w//2
        ans*=2
    while not h%2:
        h=h//2
        ans*=2
    if ans>=n:
        print("YES")
    else:
        print("NO")
