n,x = map(int,input().split())
ans = 0
for i in range(n):
    s,d = input().split()
    if s == "+":
        x+=int(d)
    else:
        if int(d)>x:
            ans+=1
        else:
            x -= int(d)
print("{} {}".format(x,ans))
