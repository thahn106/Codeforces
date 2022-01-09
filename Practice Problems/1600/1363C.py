for t in range(int(input())):
    n,x = map(int,input().split())
    dx = 0
    for i in range(n-1):
        u,v = map(int,input().split())
        if u == x or v ==x:
            dx +=1
    if dx <=1 or (n-1)%2:
        print("Ayush")
    else:
        print("Ashish")
