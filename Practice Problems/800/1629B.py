for t in range(int(input())):
    l,r,k = map(int,input().split())
    if l==r:
        if l==1:
            print("NO")
        else:
            print("YES")
    else:
        if (r-l+1) - ((r//2)-(l-1)//2)<=k:
            print("YES")
        else:
            print("NO")
