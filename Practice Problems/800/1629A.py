for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for ai,bi in  sorted(list(zip(a,b))):
        if ai<=k:
            k+=bi
        else:
            break
    print(k)
