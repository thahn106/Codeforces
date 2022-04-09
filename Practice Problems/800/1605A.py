for t in range(int(input())):
    a = list(map(int,input().split()))
    if (sum(a)-3*a[1])%3==0:
        print(0)
    else:
        print(1)
