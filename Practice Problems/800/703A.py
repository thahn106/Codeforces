a,b = 0,0
for t in range(int(input())):
    m,c = map(int,input().split())
    if m>c:
        a+=1
    elif c>m:
        b+=1
if a>b:
    print("Mishka")
elif b>a:
    print("Chris")
else:
    print("Friendship is magic!^^")
