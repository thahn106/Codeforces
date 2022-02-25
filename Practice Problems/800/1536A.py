for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    neg = False
    for i in a:
        if i<0:
            neg = True
            break
    if neg:
        print("NO")
    else:
        print("YES")
        print(101)
        print(*list(range(101)))
