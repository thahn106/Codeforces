n = int(input())
nums = list(map(int,input().split()))

r,g,c = 0,n,n
for a in nums:
    if a==0:
        r,g,c = min(c,g,r)+1, n, n
    elif a==1:
        r,g,c = min(c,g,r)+1,n ,min(r,g)
    elif a==2:
        r,g,c = min(c,g,r)+1,min(r,c),n
    else:
        r,g,c = min(c,g,r)+1,min(r,c),min(r,g)
print(min(c,g,r))
