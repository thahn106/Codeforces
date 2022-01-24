for t in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    found = False
    for i in a:
        if i in b:
            found = True
            print("YES")
            print("1 {}".format(i))
            break
    if not found:
        print("NO")
