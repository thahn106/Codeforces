for t in range(int(input())):
    n = int(input())
    r, d = divmod(n,3)
    a,b = r,r
    if d%3==1:
        a+=1
    elif d%3==2:
        b+=1
    print("{} {}".format(a,b))
