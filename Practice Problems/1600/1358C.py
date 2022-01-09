for t in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    x = x2-x1+1
    y = y2-y1+1
    print((min(x,y)-1)*(max(x,y)-1)+1)
