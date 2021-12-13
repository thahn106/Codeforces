k,r = [int(x) for x in input().split()]
i=0
while i<10:
    i+=1
    if (i*k)%10==0 or (i*k)%10==r:
        print(i)
        i=20
