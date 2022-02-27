a,b = map(int,input().split())
A,B,T = 0,0,0
for i in range(1,7):
    x = abs(a-i)
    y = abs(b-i)
    if x<y:
        A+=1
    elif y<x:
        B+=1
    else:
        T+=1
print(A,T,B)
