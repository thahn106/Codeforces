for t in range(int(input())):
    a,b = map(int,input().split())
    d = abs(a-b)
    if not d:
        print("0 0")
    else:
        m = min(a%d, -a%d)
        print(d,m)