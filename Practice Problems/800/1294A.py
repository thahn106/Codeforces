for t in range(int(input())):
    a,b,c,n = map(int,input().split())
    s = (a+b+c+n)
    if s%3==0 and max(a,b,c)*3<=s:
        print("YES")
    else:
        print("NO") 
