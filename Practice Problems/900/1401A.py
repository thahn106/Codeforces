for t in range(int(input())):
    n,k = map(int,input().split())
    if n >= k:
        if (n-k)%2:
            print(1)
        else:
            print(0)
    else:
        print(k-n)
