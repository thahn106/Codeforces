for t in range(int(input())):
    b,p,f = map(int,input().split())
    h,c = map(int,input().split())
    b= b//2
    if c>h:
        ch = min(f, b)
        b -= ch
        ha = min(p,b)
    else:
        ha = min(p,b)
        b -= ha
        ch = min(f, b)
    print(h*ha+c*ch)
