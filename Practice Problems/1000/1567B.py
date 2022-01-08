arr = [i for i in range(300000)]
mex=[0 for i in range(300000)]
x = 0
for i in arr:
    x = x^i
    mex[i] = x

for t in range(int(input())):
    a,b= map(int,input().split())
    x = mex[(a-1)]
    if x == b:
        print(a)
    elif b^x == a:
        print(a+2)
    else:
        print(a+1)
