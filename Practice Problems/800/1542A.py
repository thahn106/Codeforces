for t in range(int(input())):
    n = int(input())
    o = 0
    e = 0
    for i in list(map(int,input().split())):
        if i%2:
            o+=1
        else:
            e+=1
    if o == e:
        print("YES")
    else:
        print("NO")
