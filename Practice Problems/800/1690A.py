for t in range(int(input())):
    n = int(input())
    d,r = divmod(n,3)
    if r == 0:
        print(d,d+1,d-1)
    elif r == 1:
        print(d,d+2,d-1)
    else:
        print(d+1,d+2,d-1)
