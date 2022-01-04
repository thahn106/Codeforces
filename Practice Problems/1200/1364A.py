for t in range(int(input())):
    n,x = map(int,input().split())
    a =list(map(int,input().split()))
    a = [e%x for e in a]
    if max(a)==0:
        print(-1)
    else:
        if sum(a)%x:
            print(n)
        else:
            i,j = 0,0
            while a[i]==0:
                i+=1
            while a[n-1-j]==0:
                j+=1
            print(n-min(i+1,j+1))
