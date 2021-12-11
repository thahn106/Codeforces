for t in range(int(input())):
    n,a,b = [int(x) for x in input().split()]
    m = (n-1)//2
    possible = True
    if a > m or b > m or (a+b)>n-2:
        possible = False
    if abs(a-b)>1:
        possible = False
    if possible:
        num = [0 for i in range(n)]
        if a==b:
            i = a+b
            j = 1
            while(i<n):
                num[i] = j
                j+=1
                i+=1
            i=0
            while(i<a+b):
                num[i]=j
                j+=1
                i+=2
            i=1
            while(i<a+b):
                num[i]=j
                j+=1
                i+=2
        else:
            i = n -1
            j = 1
            while(i>a+b):
                num[i]=j
                i-=1
                j+=1
            i = 0
            while(i<a+b):
                num[i]=j
                i+=2
                j+=1
            i = 1
            while(i<=a+b):
                num[i]=j
                i+=2
                j+=1
            if b > a:
                num = [n+1-x for x in num]
        print(" ".join([str(x) for x in num]))
    else:
        print(-1)
