a,b,s = map(int,input().split())
if (a+b+s)%2 or abs(a)+abs(b)>s:
    print("No")
else:
    print("Yes")
