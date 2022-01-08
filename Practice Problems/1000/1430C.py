for t in range(int(input())):
    n = int(input())
    ans = 0
    print(2)
    for i in range(n-1):
        a,b = n-i+1,n-i-1
        if i==0:
            a-=1
        print("{} {}".format(a,b))
