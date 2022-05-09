for t in range(int(input())):
    a,b,c,x,y = map(int,input().split())
    if c >= max(0, x-a)+max(0, y-b):
        print("YES")
    else:
        print("NO")
