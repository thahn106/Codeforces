for t in range(int(input())):
    n = int(input())
    s = input()
    o = sum(list(map(int,list(s))))
    z = n-o
    if o>1 or z>1:
        print("NO")
    else:
        print("YES")
