for t in range(int(input())):
    l = list(map(int,input().split()))
    l.sort()
    if l[0]+l[1]==l[2]:
        print("YES")
    elif l[0]==l[1] and l[2]%2==0:
        print("YES")
    elif l[2]==l[1] and l[0]%2==0:
        print("YES")
    else:
        print("NO")
