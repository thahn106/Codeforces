m,s = map(int,input().split())
if m==1 and s==0:
    print("0 0")
elif s<1 or s>9*m:
    print("-1 -1")
else:
    large = [0 for i in range(m)]
    i=0
    t = s
    while s>0:
        if s>9:
            large[i]+=9
            s-=9
        else:
            large[i]+=s
            s = 0
        i+=1
    small = [0 for i in range(m)]
    small[-1]=1
    s = t-1
    i=0
    while s>0:
        if s>9:
            small[i]+=9
            s-=9
        else:
            small[i]+=s
            s = 0
        i+=1
    small.reverse()
    small = "".join(map(str, small))
    large = "".join(map(str, large))
    print("{} {}".format(small, large))
