l,r = 0,0
for n in range(int(input())):
    x,y = map(int, input().split())
    if x<0:
        l+=1
    else:
        r+=1

if min(l,r)>1:
    print('No')
else:
    print("Yes")
