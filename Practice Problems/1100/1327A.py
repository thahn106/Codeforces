for t in range(int(input())):
    n,k = map(int,input().split())
    if (n-k)%2 or n<k**2:
        print("NO")
    else:
        print("YES")
