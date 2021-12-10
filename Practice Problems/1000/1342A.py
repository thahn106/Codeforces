for t in range(int(input())):
    x,y = [int(x) for x in input().split()]
    a,b = [int(x) for x in input().split()]
    if 2*a <= b :
        cost = (x+y)*a
    else:
        cost = min(x,y)*b+(max(x,y)-min(x,y))*a
    print(cost)
