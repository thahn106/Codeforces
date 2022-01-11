for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    alleven = True
    allodd = True
    for i in a:
        if i%2:
            alleven = False
        else:
            allodd =False
    if alleven or (allodd and n%2==0):
        print("NO")
    else:
        print("YES")
