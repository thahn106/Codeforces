for t in range(int(input())):
    a = list(map(int,input().split()))
    a.sort()
    if a[1]!=a[2]:
        print("NO")
    else:
        print("YES")
        print("{} {} {}".format(a[0],a[0],a[2]))
