for q in range(int(input())):
    a,b,c = map(int,input().split())
    print(min(a,b,(a+b+c)//3))
