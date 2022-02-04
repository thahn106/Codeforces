for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    odd = a[0]%2
    same = True
    for i in a:
        if (i-odd)%2:
            same= False
            break
    if same:
        print("YES")
    else:
        print("NO")
