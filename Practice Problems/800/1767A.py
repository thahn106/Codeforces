for t in range(int(input())):
    input()
    x = []
    y = []
    for i in range(3):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    if len(set(x)) == 2 and len(set(y))==2:
        print("NO")
    else:
        print("YES")