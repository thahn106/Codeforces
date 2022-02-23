for q in range(int(input())):
    l1,r1,l2,r2 = map(int,input().split())
    a = l1
    if l2 == a:
        b = r2
    else:
        b = l2
    print(a,b)
